# GetWeather
Get an SMS every morning with the forecast for the day

Attempting to build an application that pulls weather data from a website every morning and forwards the data in SMS format to a phone number.

Basic workflow:
1. -- forward input through a SMTP to cell phone number via carrier Gateway
  1.1 -- this smtp use via python was presenting more issues than my skill level could efficiently accomodate; adjusted method to use twilio api
2. -- timer that runs the code above daily at a specified time
 2.1 -- will be last item to complete; merge with item 5
3. -- collects data from the html of a specific URL, (edit: the following needs to be it's own item, see item 4) then forwards to the program on item 1
4. -- take data from scraper and send/get/whatever to sms script
5. -- timer(s) to execute the code above

Update: Dec 6 2021,
While the twilio API made sending a text via python very easy, and a python script running with the BeautifulSoup dependancy also made scraping a weather site simple, there were a few problems that have led me to reapproach this project:
1. The script for use with the twilio API requires a string format to be entered for the body of the text message. This doesn't accomodate the function that I created that gets the current temp for my zipcode.
2. Setting a daily cadence to run this was also not difficult, but requires the script to run constantly on my local device, or a server that I do not have haha.

Time to explore other ways to go about this...
