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

		# create a queue to store the scheduled text messages
		self._dq = DefaultQueue(lambda: "DEFAULT ARG")

	def _send_text(self) -> None:
		"""Send the next text message in _dq and log necessary information to console."""
		text_message = self._dq.pop_left()

		# send text and store the returned MessageInstance
		twilio_message = send_text(text_message)

		logger.info("text sent: {}".format(text_message))
		logger.info("sid: {}".format(twilio_message.sid))

	def run(self) -> None:
		"""Run the TextDaemon thread. This thread runs forever and sends a text message once a day."""
		logger.info("Text daemon thread starting")

		while True:

			while datetime.datetime.now() < self.send_time:
				time.sleep(5)

				# retrieve any messages from the server_to_text queue and respond accordingly
				self.server_to_text.empty_and(log_and_put(self._dq))
				logger.info("Text daemon is alive. Watch fibonacci: {}".format(next(fib_gen)))

			# send a text message and reset the send_time
			self._send_text()
			self.send_time += datetime.timedelta(seconds=self.period)
