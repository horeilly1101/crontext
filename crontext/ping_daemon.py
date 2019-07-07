
from threading import Thread
import logging
import time

import requests

from config import PingDaemonConfig


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


class PingDaemon(Thread):
    def __init__(self):
        super().__init__(daemon=True)

    def run(self) -> None:
        LOGGER.info("Ping Daemon is starting.")
        while True:
            time.sleep(60 * 25)  # sleep for 25 minutes

            requests.get(PingDaemonConfig.APP_URL)
