#first, import all necessary libraries
from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import requests
import random
from pandas import DataFrame as df

#list of authors and quotes
authors = []
quotes = []
#list of urls
urls = [f"http://quotes.toscrape.com/page/{i}/" for i in range(1,11)]
#list for randomizing request rate
rate = [i/10 for i in range(10)]
#iterating through URLs
for url in urls:
    #accessing the webpage
    page = requests.get(url)
    #getting the page's content in pure html
    soup = bs(page.content)
    #adding the authors and quotes to their lists
    authors.extend([i.text for i in soup.find_all(class_='author')])
    quotes.extend([i.text for i in soup.find_all(class_='text')])
    #checking to see if we hit required number of quotes then breaking the loop
    if len(quotes) >= 52:
        break
    #randomizing request rate
    # use when doing in real life -- time.sleep(random.choice(rate))
    #creating a dataframe to store scraped info
    df = pd.DataFrame()
    #storing the quotes and authors in respective columns
    df['Authors'] = authors
    df['Quotes'] = quotes
    print(df)
