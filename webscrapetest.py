#first, import all necessary libraries
from bs4 import BeautifulSoup as bs
import time
import requests

realfeel = ()
url = (f"https://www.accuweather.com/en/us/littleton/80120/weather-forecast/332178")
#scrapin' away
def getwethr():
    #accessing the webpage
    page = requests.get(url)
    #getting the page's content in pure html
    soup = bs(page.content)
    #getting RealFeel text results
    results = soup.find_all(class_="real-feel")
    #view results
    print(results())
    #-DISABLED WHILE TESTING time.sleep(86400)
    #-DISABLED WHILE TESTING print(results.prettify())
