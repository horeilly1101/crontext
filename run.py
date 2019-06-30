"""run the server"""

import sys
import datetime

from crontext.server import AppThread
from crontext.worker.text_daemon import TextDaemon
from crontext.safe_queue import SafeQueue


def _main():
    # create the message channels between the server and the worker
    server_to_worker = SafeQueue()
    worker_to_server = SafeQueue()

    app_thread = AppThread(server_to_worker, worker_to_server)
    fib_thread = TextDaemon(server_to_worker,
                            datetime.datetime.now() + datetime.timedelta(seconds=30),
                            30)

    fib_thread.start()
    app_thread.start()

    try:
        fib_thread.join()
        app_thread.join()

    except (KeyboardInterrupt, SystemExit):
        sys.exit()


if __name__ == "__main__":
    _main()
