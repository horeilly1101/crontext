"""File that creates and configures the """

import logging

from flask import Flask

from config import ServerConfig
from crontext.safe_queue import SafeQueue
from crontext.server.models import db, migrate
from crontext.server.controllers.routes import server, TextForm

# Create a custom logger
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


def create_app(server_to_worker: SafeQueue, worker_to_server: SafeQueue) -> Flask:
    """Application factory to create and configure the server app.

    :param server_to_worker: a channel from the server thread to the worker thread
    :param worker_to_server: a channel from the worker thread to the server thread
    :return: flask web app
    """
    app = Flask(__name__)

    # add config variables
    app.config.from_object(ServerConfig)

    # connect the database
    db.init_app(app)
    migrate.init_app(app)

    # create db tables, if they don't already exist
    with app.app_context():
        db.create_all()

    # store the message channels as extensions
    app.extensions["server_to_worker"] = server_to_worker
    app.extensions["worker_to_server"] = worker_to_server

    # add the routes
    app.register_blueprint(server)

    return app
