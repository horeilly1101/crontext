"""File to contain all of the necessary config information for the project"""
import os


class ServerConfig:
	pass


class SchedulerConfig:
	"""Object to keep track of config variables for the project."""
	# Your Account Sid and Auth Token from twilio.com/user/account
	account_sid = os.environ['TWILIO_ACCOUNT_SID']
	auth_token = os.environ['TWILIO_AUTH_TOKEN']

	# the phone number sending the text message (should be associated with your twilio
	# account)
	from_number = os.environ['TWILIO_FROM_NUMBER']

	# the phone number receiving the text
	to_number = os.environ['TWILIO_TO_NUMBER']
