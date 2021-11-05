# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['AC0f8a14d8a3f98dfd20a03453c51aba9b']
auth_token = os.environ['252fc28c0245204dfc870f5c2645e915']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="SMS push weather service test",
                     from_='+18506018836',
                     to='+17145590485'
                 )

print(message.sid)
