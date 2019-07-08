
from threading import Thread
import logging
import time

import requests

from config import PingDaemonConfig


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


class PingDaemon(Thread):
    """Daemon thread that pings the server periodically so that the heroku dyno
    doesn't sleep.
    """
    def __init__(self):
        super().__init__(daemon=True)

    def run(self) -> None:
        """Ping the server periodically."""
        LOGGER.info("Ping Daemon is starting.")

        while True:
            # sleep for 25 minutes
            time.sleep(60 * 25)
            # ping the server
            requests.get(PingDaemonConfig.APP_URL)
