"""run the server"""

import sys

from crontext.producer import app_thread
from crontext.consumer import fib_thread


def _main():
	fib_thread.start()
	app_thread.start()

	try:
		fib_thread.join()
		app_thread.join()

	except KeyboardInterrupt:
		sys.exit(1)


if __name__ == "__main__":
	_main()
