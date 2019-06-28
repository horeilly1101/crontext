"""run the server"""

import sys
import datetime

from crontext.server import AppThread
from crontext.text_daemon import TextDaemon
from crontext.safe_queue import SafeQueue


def _main():
    app_thread = AppThread()
    fib_thread = TextDaemon(app_thread.server_to_text,
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
