"""run the server"""

import logging
import sys

from crontext.app import app_thread
from crontext.schedule_task import fib_thread

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create handler
c_handler = logging.StreamHandler()

# Create formatter and add it to handler
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)

# Add handler to the logger
logger.addHandler(c_handler)


def _main():
	logger.info("Fib thread starting")
	fib_thread.start()
	
	logger.info("App thread starting")
	app_thread.start()

	try:
		fib_thread.join()
		app_thread.join()

	except KeyboardInterrupt:
		logger.info("Fib thread shutting down")
		sys.exit(1)


if __name__ == "__main__":
	_main()
