# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
#NOTE!- in order for this code to work I had to first rung this in terminal:
# export TWILIO_ACCOUNT_SID=*my actual sid*
# export TWILIO_AUTH_TOKEN=*my actual authtoken*
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="SMS push weather service test",
                     from_='+18506018836',
                     to='+17145590485'
                 )

print(message.sid)
