#first, import all necessary libraries
# Download the helper library from https://www.twilio.com/docs/python/install
# STEP 1. Must use virtual env for this. run- source getwethr_env/bin/activate
# Find your Account SID and Auth Token at twilio.com/console
# STEP 2. in order for this code to work I had to first run this in terminal:
# export TWILIO_ACCOUNT_SID=*my actual sid*
# export TWILIO_AUTH_TOKEN=*my actual auth token*
import os
from twilio.rest import Client
from bs4 import BeautifulSoup as bs
import time
import requests

url = (f"https://weather.com/weather/today/l/443bba801902adfc2e7efa8237c7ba57ad62386f06a88b9bcbe00f39d1a7c22e")
#scrapin' away
def getwethr():
    #accessing the webpage
    page = requests.get(url)
    #getting the page's content in pure html
    soup = bs(page.content)
    #getting RealFeel text results
    results = soup.find(class_="CurrentConditions--tempValue--3a50n")
    #view results
    print(results.text)
    #-DISABLED WHILE TESTING time.sleep(86400)
    #-DISABLED WHILE TESTING print(results.prettify())

getwethr()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body='',
                     from_='+18506018836',
                     to='+17145590485'
                 )

print(message.sid)
