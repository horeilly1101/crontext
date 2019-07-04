import datetime
import logging
import time
from threading import Thread

from crontext.worker.default_queue import DefaultQueue
from crontext.data_packet import ReceiptPacket

LOGGER = logging.getLogger(__name__)


class TextDaemon(Thread):
	"""A daemon thread that sends a text message once a day, every day."""

	def __init__(self, server_to_worker, worker_to_server, start_date_time, period):
		super().__init__(daemon=True)
		self.server_to_worker = server_to_worker
		self.worker_to_server = worker_to_server
		self.send_time = start_date_time
		self.period = period

		# create a queue to store the scheduled text messages
		self._dq = DefaultQueue(lambda: "DEFAULT ARG")

	def _send_text(self) -> None:
		"""Send the next text message in _dq and log necessary information to console."""
		text_message = self._dq.pop_left()

		# ------------------
		# In development: send a text
		# ------------------
		# # send text and store the returned MessageInstance
		# twilio_message = send_text(text_message)
		#
		# LOGGER.info("text sent: {}".format(text_message))
		# LOGGER.info("sid: {}".format(twilio_message.sid))

		LOGGER.info(text_message)

		# self.worker_to_server.put(ReceiptPacket(datetime.datetime.now(), text_message.id))

	def run(self) -> None:
		"""Run the TextDaemon thread. This thread runs forever and sends a text message once a day."""
		LOGGER.info("Text daemon thread starting")

		while True:

			while datetime.datetime.now() < self.send_time:
				time.sleep(5)

				# retrieve any messages from the server_to_text queue and respond accordingly
				self.server_to_worker.remove_all_and(self._dq.add_right)
				LOGGER.info("Text daemon is alive")

			# send a text message and reset the send_time
			self._send_text()
			self.send_time += datetime.timedelta(seconds=self.period)
