# GetWeather
Get an SMS every morning with the forecast for the day

Attempting to build an application that pulls weather data from a website every morning and forwards the data in SMS format to a phone number.

Basic workflow:
1. -- forward input through a SMTP to cell phone number via carrier Gateway
2. -- timer that runs the code above daily at a specified time
3. -- collects data from the script of a specific URL, then forwards to the program on item 1
4. -- timer to execute the code on item 3 (unless the timer can be built in, same for itme 2)
