"""File that creates and configures the """

import logging
from threading import Thread
import os

from flask import Flask

from config import ServerConfig
from crontext.safe_queue import SafeQueue
from crontext.server.text_form import TextForm
from crontext.server.routes import server
from crontext.server.models import db, migrate

# Create a custom logger
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


def create_app(server_to_worker: SafeQueue, worker_to_server: SafeQueue) -> Flask:
	"""Application factory to create and configure the server app.

	:param server_to_worker: a channel from the server thread to the worker thread
	:param worker_to_server: a channel from the worker thread to the server thread
	"""
	app = Flask(__name__)

	# add config variables and blueprint routes
	app.config.from_object(ServerConfig)
	app.register_blueprint(server)

	# connect the database
	db.init_app(app)
	migrate.init_app(app)

	# store the message channels as extensions
	app.extensions["server_to_worker"] = server_to_worker
	app.extensions["worker_to_server"] = worker_to_server

	return app


class AppThread(Thread):
	"""Thread that runs the server app."""
	def __init__(self, server_to_worker, worker_to_server):
		"""Initialize the AppThread."""
		super().__init__(daemon=True)
		self._app = create_app(server_to_worker, worker_to_server)

	def run(self) -> None:
		"""Run the server."""
		LOGGER.info("Flask App staring")
		self._app.run(port=os.environ["PORT"])
