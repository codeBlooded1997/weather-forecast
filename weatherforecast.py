import pandas as pd
import requests
from bs4 import BeautifulSoup

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

# writng into a csv file
# uncomment to create csv file
#weather_stuff.to_csv('weather.csv')
