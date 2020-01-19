import pandas as pd
import requests
from bs4 import BeautifulSoup

# grabbing page
url = 'https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

week = soup.find(id="seven-day-forecast-container")
items = week.find_all(class_ = "tombstone-container")

#print(items[0].find(class_ = "period-name").get_text())
#print(items[0].find(class_ = "short-desc").get_text())
#print(items[0].find(class_ = "temp").get_text())

days = [item.find(class_ = "period-name").get_text() for item in items]
short_describtions = [item.find(class_ = "short-desc").get_text() for item in items]
tempratures = [item.find(class_ = "temp").get_text() for item in items]

# making pandas dataframe
weather_stuff = pd.DataFrame(
    {
        'period' : days,
        'description' : short_describtions,
        'temperature' : tempratures,
    })
print(weather_stuff)

# writng into a csv file
weather_stuff.to_csv('weather.csv')