# STEP 1. run these in terminal:
# export TWILIO_ACCOUNT_SID=*my actual sid*
# export TWILIO_AUTH_TOKEN=*my actual auth token*
# STEP 2. Must use virtual env for this:
# In terminal: source getwethr_env/bin/activate

import os
# from twilio.rest import Client
from bs4 import BeautifulSoup as bs
import time
import requests

url = (f"https://weather.com/weather/today/l/443bba801902adfc2e7efa8237c7ba57ad62386f06a88b9bcbe00f39d1a7c22e")
def getwethr():
    page = requests.get(url)
    soup = bs(page.content)
    results = soup.find(class_="CurrentConditions--tempValue--3a50n")
    #view results
    x = str(results.text)
    return x
#   DISABLED WHILE TESTING- time.sleep(86400)

y = getwethr()

# !!! the code below is for using the Twilio API to send a SMS

# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)
#
# message = client.messages \
#                .create(
#                     body=y,
#                     from_='+18506018836',
#                     to='+17145590485'
#                 )
#
# print(message.sid)
