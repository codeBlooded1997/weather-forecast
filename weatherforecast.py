import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

date = datetime.datetime.now()
# grabbing page
url = 'https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999'
page = requests.get(url)
print('Grabbing')
soup = BeautifulSoup(page.content, "html.parser")

# parsing data
week = soup.find(id="seven-day-forecast-container")
items = week.find_all(class_ = "tombstone-container")

days = [item.find(class_ = "period-name").get_text() for item in items]
short_describtions = [item.find(class_ = "short-desc").get_text() for item in items]
tempratures = [item.find(class_ = "temp").get_text() for item in items]

# pandas dataframe
weather_stuff = pd.DataFrame(
    {
        'period' : days,
        'description' : short_describtions,
        'temperature' : tempratures,
    })
print(weather_stuff)
print()


# creating extention for csv file
extention = str(date.strftime("%c"))
# uncomment to create csv file
weather_stuff.to_csv(extention + '-weather.csv')

print("CSV FILE CREATED")

# Sending SMS
account_sid = "AC81b4362f605c6398a48da412dcff6926"
auth_token  = "84aa917ee50e1f59bf7c1d1264f7d1c3"
client = Client(account_sid, auth_token)
message = client.messages.create(
   to="+14387004763",
   from_="+16194326457",
   body=str(weather_stuff)
)

print()
print("A TEXT MASSAGE HAS BEEN SEND.")