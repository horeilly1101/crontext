"""File that creates and configures the """

import logging

from flask import Flask

from config import ServerConfig
from crontext.safe_channel import SafeChannel
from crontext.server.models import db, migrate
from crontext.server.controllers.routes import server, TextForm

# Create a custom logger
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


def create_app(safe_channel: SafeChannel) -> Flask:
    """Application factory to create and configure the server app.

    :param safe_channel: a channel between the server thread and the worker thread
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
    app.extensions["safe_channel"] = safe_channel

    # add the routes
    app.register_blueprint(server)

    return app
