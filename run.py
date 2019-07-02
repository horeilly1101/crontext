"""run the server"""

import sys
import datetime
import os

from crontext.server import create_app
from crontext.worker.text_daemon import TextDaemon
from crontext.safe_queue import SafeQueue


def _main():
    # create the message channels between the server and the worker
    server_to_worker = SafeQueue()
    worker_to_server = SafeQueue()

    server = create_app(server_to_worker, worker_to_server)
    worker = TextDaemon(server_to_worker,
                        datetime.datetime.now() + datetime.timedelta(seconds=30),
                        30)

    worker.start()

    try:
        server.run(host="0.0.0.0", port=os.environ["PORT"])
        worker.join()

    except (KeyboardInterrupt, SystemExit):
        sys.exit()


if __name__ == "__main__":
    _main()
