import logging
import datetime
import sys

from crontext.server import create_app
from crontext.worker.text_daemon import TextDaemon
from crontext.safe_channel.safe_queue import SafeQueue

# Configure the logger
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

handler = logging.StreamHandler()

logger_format = logging.Formatter('%(levelname)s - %(name)s - %(asctime)s - %(message)s')
handler.setFormatter(logger_format)

LOGGER.addHandler(handler)


def run_crontext(host: str, port: int) -> None:
    """
    Run the crontext process.
    :param host: host computer address (e.g. "127.0.0.1")
    :param port: port the web server will listen on (e.g. 1357)
    """
    # create the message channels between the server and the worker
    server_to_worker = SafeQueue()
    worker_to_server = SafeQueue()

    # create the server app and the worker
    app = create_app(server_to_worker, worker_to_server)
    worker = TextDaemon(server_to_worker, worker_to_server, datetime.datetime.now() + datetime.timedelta(seconds=30), 30)

    # star the worker in a background thread
    worker.start()

    try:
        # run the app and block until both tasks end
        app.run(host=host, port=port)
        worker.join()

    except (KeyboardInterrupt, SystemExit):
        sys.exit()
