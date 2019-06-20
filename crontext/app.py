"""defines the structure of the main app"""

import logging
from threading import Thread
from flask import Flask

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

_app = Flask(__name__)


@_app.route("/")
def index():
	logging.info("HULLO")
	return "Hello, world"


# put the app in its own thread
app_thread = Thread(target=_app.run, daemon=True)

if __name__ == "__main__":
	_app.run()  # run the app
