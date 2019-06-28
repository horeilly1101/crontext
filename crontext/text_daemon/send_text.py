"""File that contains the send_text function."""

import os
import logging
from twilio.rest import Client

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# the phone number sending the text message (should be associated with your twilio
# account)
from_number = os.environ['TWILIO_FROM_NUMBER']

# the phone number receiving the text
to_number = os.environ['TWILIO_TO_NUMBER']


def send_text(text_message: str) -> str:
	"""
	Send the input text message to the specified number, using the Twilio API.

	:param text_message: message to be sent
	"""
	client = Client(account_sid, auth_token)

	# create and send a text message
	message = client.messages \
		.create(
			body=text_message,
			from_=from_number,
			to=to_number
		)

	return message.sid
