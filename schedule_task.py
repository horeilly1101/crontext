import logging
from threading import Thread
import time
import sys

import logging

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
try:
	hw_thread = Thread(target=target, daemon=True)
	logger.info("Process starting")
	hw_thread.start()
	hw_thread.join()
except KeyboardInterrupt:
	logger.info("Shutting down threads")
	sys.exit(1)
