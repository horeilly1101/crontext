"""File that contains the send_text function."""

import logging
from twilio.rest import Client

from config import SchedulerConfig

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

# Your Account Sid and Auth Token from twilio.com/user/account
ACCOUNT_SID = SchedulerConfig.account_sid
AUTH_TOKEN = SchedulerConfig.auth_token

# the phone number sending the text message (should be associated with your twilio
# account)
FROM_NUMBER = SchedulerConfig.from_number

# the phone number receiving the text
TO_NUMBER = SchedulerConfig.to_number


def send_text(text_message: str) -> "MessageInstance":
	"""
	Send the input text message to the specified number, using the Twilio API.

	:param text_message: message to be sent
	"""
	client = Client(ACCOUNT_SID, AUTH_TOKEN)

	# create and send a text message
	message = client.messages \
		.create(
			body=text_message,
			from_=FROM_NUMBER,
			to=TO_NUMBER
		)

	return message
