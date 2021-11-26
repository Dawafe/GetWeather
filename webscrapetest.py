#first, import all necessary libraries
from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import requests
from pandas import DataFrame as df

realfeel = []
#list of urls
urls = [f"https://www.accuweather.com/en/us/littleton/80120/weather-forecast/332178"]
#iterating through URLs
for url in urls:
    #accessing the webpage
    page = requests.get(url)
    #getting the page's content in pure html
    soup = bs(page.content)
    #adding the RealFeel temp to the dataframe
    realfeel.extend([i.text for i in soup.find_all(class_='real-feel')])
    #creating a dataframe to store scraped info
    df = pd.DataFrame()
    #storing the text in a dataframe
    df['Temp'] = realfeel
    print(df)
    #-DISABLED WHILE TESTING time.sleep(86400)
    #-DISABLED WHILE TESTING print(df)
