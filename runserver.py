"""run the server"""

import sys

from crontext.server import app_thread
from crontext.text_daemon import Consumer


def _main():
	fib_thread = Consumer()
	fib_thread.start()
	app_thread.start()

	try:
		fib_thread.join()
		app_thread.join()

	except (KeyboardInterrupt, SystemExit):
		sys.exit()


if __name__ == "__main__":
	_main()
