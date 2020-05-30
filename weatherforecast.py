import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client



# Your number goes here:
TWILIO_NUMBER = 'TWILIO NUMBER'
RECIEVER_NUMBER = 'RECIEVER NUMBER'
ACCOUNT_SID = 'ACCOUNT SID'
AUTH_TOKEN = 'AUTH TOKEN'



date = datetime.datetime.now()
# Grabbing page
url = 'https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999'
page = requests.get(url)
print('Grabbing')
soup = BeautifulSoup(page.content, "html.parser")

# Parsing data
week = soup.find(id="seven-day-forecast-container")
items = week.find_all(class_ = "tombstone-container")

days = [item.find(class_ = "period-name").get_text() for item in items]
short_describtions = [item.find(class_ = "short-desc").get_text() for item in items]
tempratures = [item.find(class_ = "temp").get_text() for item in items]

# Pandas dataframe
weather_stuff = pd.DataFrame(
    {
        'period' : days,
        'description' : short_describtions,
        'temperature' : tempratures,
    })
print(weather_stuff)
print()


# Creating extention for csv file.
extention = str(date.strftime("%c"))
# Writing extracted data in csv file.
weather_stuff.to_csv(extention + '-weather.csv')

print("CSV FILE CREATED")

# Sending SMS
account_sid = ACCOUNT_SID
auth_token  = AUTH_TOKEN
client = Client(account_sid, auth_token)
message = client.messages.create(
   to = RECIEVER_NUMBER,
   from_ = WILIO_NUMBER,
   body=str(weather_stuff)
)

print()
print("A TEXT MASSAGE HAS BEEN SEND.")
