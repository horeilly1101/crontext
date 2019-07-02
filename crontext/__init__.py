import logging
import datetime
import sys

from crontext.server import create_app
from crontext.worker.text_daemon import TextDaemon
from crontext.safe_queue import SafeQueue

# Create a custom logger
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

# Create handler
c_handler = logging.StreamHandler()

# Create formatter and add it to handler
c_format = logging.Formatter('%(levelname)s - %(name)s - %(asctime)s - %(message)s')
c_handler.setFormatter(c_format)

# Add handler to the logger
LOGGER.addHandler(c_handler)


def run_crontext(host, port):
	# create the message channels between the server and the worker
	server_to_worker = SafeQueue()
	worker_to_server = SafeQueue()

	app = create_app(server_to_worker, worker_to_server)
	worker = TextDaemon(server_to_worker, datetime.datetime.now() + datetime.timedelta(seconds=30), 30)

	worker.start()

	try:
		app.run(host=host, port=port)
		worker.join()

	except (KeyboardInterrupt, SystemExit):
		sys.exit()
