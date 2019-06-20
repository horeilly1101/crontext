
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# the phone number sending the text message (should be associated with your twilio 
# account)
from_number = os.environ['TWILIO_FROM_NUMBER']

# the phone number receiving the text
to_number = os.environ['TWILIO_TO_NUMBER']

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_=from_number,
                     to=to_number
                 )

print(message.sid)
