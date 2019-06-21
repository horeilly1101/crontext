"""defines the structure of the main app"""

import logging
from threading import Thread
from flask import Flask

from crontext import lifo

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

_app = Flask(__name__)


@_app.route("/")
def index():
	lifo.put("Yo whats up")
	return "Hello, world"


def target():
	logger.info("Flask App staring")
	_app.run(port=5678)


# put the app in its own thread
app_thread = Thread(target=target, daemon=True)

if __name__ == "__main__":
	# run the app
	_app.run()
