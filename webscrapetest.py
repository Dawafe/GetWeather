#first, import all necessary libraries
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
