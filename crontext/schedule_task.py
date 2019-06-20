import logging
from threading import Thread
import time
import sys

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


def fibonacci():
	a, b = (0, 1)
	while True:
		a, b = (b, a + b)
		yield a


fib_gen = fibonacci()


def task():
	logger.info("I'm alive. Watch fibonacci: {}".format(next(fib_gen)))


def target():
	while True:
		time.sleep(1)
		task()


fib_thread = Thread(target=target, daemon=True)


def _main():
	try:
		logger.info("Fib thread starting")
		fib_thread.start()
		fib_thread.join()

	except KeyboardInterrupt:
		logger.info("Fib thread shutting down")
		sys.exit(1)


if __name__ == "__main__":
	_main()
