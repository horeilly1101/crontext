"""defines the structure of the main app"""

import logging
from threading import Thread
from flask import Flask

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

_app = Flask(__name__)


@_app.route("/")
def index():
	return "Hello, world"


def target():
	logger.info("Flask App staring")
	_app.run()


# put the app in its own thread
app_thread = Thread(target=target, daemon=True)

if __name__ == "__main__":
	_app.run()  # run the app
