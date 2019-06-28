import logging
from threading import Thread
import time
import datetime

from crontext.text_daemon.default_queue import DefaultQueue
from crontext.text_daemon.send_text import send_text

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def fibonacci():
	a, b = (0, 1)
	while True:
		a, b = (b, a + b)
		yield a


fib_gen = fibonacci()


def log_and_put(q):
	def put(message):

		logger.info("Add to queue: {}".format(message))
		q.add_right(message)

	return put


class TextDaemon(Thread):
	def __init__(self, server_to_text, start_date_time, period):
		super().__init__(daemon=True)
		self.server_to_text = server_to_text
		self.send_time = start_date_time
		self.period = period

		self._dq = DefaultQueue(lambda: "DEFAULT ARG")

	def _send_text(self):
		text_message = self._dq.pop_left()
		message = send_text
		logger.info("text sent: {}".format(self._dq.pop_left()))

	def run(self) -> None:
		logger.info("Text daemon thread starting")

		while True:

			while datetime.datetime.now() < self.send_time:
				time.sleep(5)
				self.server_to_text.empty_and(log_and_put(self._dq))
				logger.info("Text daemon is alive. Watch fibonacci: {}".format(next(fib_gen)))

			self._send_text()
			self.send_time += datetime.timedelta(seconds=self.period)
