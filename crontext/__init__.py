import logging
import datetime
import sys

from crontext.server import create_app
from crontext.worker.worker_daemon import WorkerDaemon
from crontext.broker import BrokerFactory
from crontext.ping_daemon import PingDaemon

# Configure the logger
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

handler = logging.StreamHandler()

logger_format = logging.Formatter('%(levelname)s - %(name)s - %(asctime)s - %(message)s')
handler.setFormatter(logger_format)

LOGGER.addHandler(handler)


def run_crontext(host: str, port: int) -> None:
    """
    Run the crontext process.
    :param host: host computer address (e.g. "127.0.0.1")
    :param port: port the web server will listen on (e.g. 1357)
    """
    # create the message channels between the server and the worker
    safe_channel_fac = BrokerFactory()

    # create the server app and the worker
    app = create_app(safe_channel_fac.make_endpoint1())
    worker = WorkerDaemon(safe_channel_fac.make_endpoint2(), datetime.datetime.now() + datetime.timedelta(seconds=30), 30)

    # start the ping daemon
    ping = PingDaemon()

    # start the worker and ping daemon in background threads
    worker.start()
    ping.start()

    try:
        # run the app and block until all tasks end (spoiler alert: they never end)
        app.run(host=host, port=port)
        worker.join()
        ping.join()

    except (KeyboardInterrupt, SystemExit):
        sys.exit()
