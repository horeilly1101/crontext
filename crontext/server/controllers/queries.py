"""File that contains various database queries and controller functions."""

import datetime

from crontext.data_packet import TextPacket, ReceiptPacket
from crontext.server import db
from crontext.server.models import TextModel


def store_and_create_message(text_input: str) -> TextPacket:
	"""Store the input text message in the database, and return a packet to be
	sent to the worker.
	:param text_input: text message input by user
	"""
	# create the model and store it in the database
	text_model = TextModel(message=text_input, created_at=datetime.datetime.now())
	db.session.add(text_model)
	db.session.commit()

	# construct and return data packet
	return TextPacket(text_input, text_model.id)


def update_text_model(receipt_packet: ReceiptPacket):
	text = db.query(TextModel).get(receipt_packet.id)

	if text is None:
		pass

	# update the sent at time in the db
	text.sent_at = receipt_packet.sent_at
	db.session.commit()