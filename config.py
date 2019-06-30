"""File to contain all of the necessary config information for the project"""
import os


class ServerConfig:
	"""Object to keep track of config variables for the server module."""
	SECRET_KEY = os.environ['SECRET_KEY'] or "change-me-or-get-hacked"

	# configure the database
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class WorkerConfig:
	"""Object to keep track of config variables for the worker module."""
	# Your Account Sid and Auth Token from twilio.com/user/account
	ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
	AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

	# the phone number sending the text message (should be associated with your twilio
	# account)
	FROM_NUMBER = os.environ['TWILIO_FROM_NUMBER']

	# the phone number receiving the text
	TO_NUMBER = os.environ['TWILIO_TO_NUMBER']
