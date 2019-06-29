"""defines the structure of the main app"""

import logging
from threading import Thread

from flask import Flask

from crontext.safe_queue import SafeQueue

# Create a custom logger
from crontext.server.text_form import TextForm

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

_app = Flask(__name__)

# _app.secret_key = os.environ['FLASK_SECRET_KEY']
_app.secret_key = 'dont-hack-me-pls'

server_to_text = SafeQueue()

import crontext.server.routes


class AppThread(Thread):
	def __init__(self):
		super().__init__(daemon=True)
		self.server_to_text = server_to_text

	def run(self) -> None:
		LOGGER.info("Flask App staring")
		_app.run(port=6789)
