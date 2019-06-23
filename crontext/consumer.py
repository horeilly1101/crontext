import logging
from threading import Thread, Lock
import time
import sys
import datetime
from crontext import fifo

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# send_time = datetime.datetime(2019, 6, 22, 12, 31)


def fibonacci():
	a, b = (0, 1)
	while True:
		a, b = (b, a + b)
		yield a


fib_gen = fibonacci()


class DefaultQueue:
	def __init__(self, default_func):
		self.inbox = []
		self.outbox = []
		self.default_func = default_func

	def add_right(self, item):
		self.inbox.append(item)

	def pop_left(self):
		if self.outbox:
			return self.outbox.pop()

		if self.inbox:
			for i in range(len(self.inbox)):
				self.outbox.append(self.inbox.pop())

			return self.outbox.pop()

		return self.default_func()


lock = Lock()

dq = DefaultQueue(lambda: "DEFAULT ARG")


class TextSender(Thread):
	def __init__(self, send_time):
		super().__init__(daemon=True)
		self.send_time = send_time

	def run(self) -> None:
		while True:
			while datetime.datetime.now() < self.send_time:
				time.sleep(1)
				logger.info("TextSender is alive")

			with lock:
				logger.info("val: {}".format(dq.pop_left()))
				self.send_time += datetime.timedelta(seconds=30)


class Consumer(Thread):
	def __init__(self):
		super().__init__(daemon=True)

	def run(self) -> None:
		logger.info("Fib thread starting")
		sender = TextSender(datetime.datetime.now() + datetime.timedelta(seconds=30))
		sender.start()

		while True:
			logger.info("Consumer is alive. Watch fibonacci: {}".format(next(fib_gen)))

			message = fifo.get()
			logger.info(message)

			with lock:
				dq.add_right(message)


def _main():
	fib_thread = Consumer()

	try:
		fib_thread.start()
		fib_thread.join()

	except KeyboardInterrupt:
		logger.info("Fib thread shutting down")
		sys.exit(1)


if __name__ == "__main__":
	_main()
