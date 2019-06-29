"""File to contain all of the necessary config information for the project"""
import os


class ServerConfig:
	"""Object to keep track of config variables for the server module."""
	DATABASE_URL = os.environ['DATEBASE_URL']


class SchedulerConfig:
	"""Object to keep track of config variables for the scheduler module."""
	# Your Account Sid and Auth Token from twilio.com/user/account
	ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
	AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

	# the phone number sending the text message (should be associated with your twilio
	# account)
	FROM_NUMBER = os.environ['TWILIO_FROM_NUMBER']

	# the phone number receiving the text
	TO_NUMBER = os.environ['TWILIO_TO_NUMBER']
