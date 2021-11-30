import pandas as pd
import requests
from bs4 import BeautifulSoup

#THIS IS A SIMPLE PROGRAM THAT SCRAPES A WEATHER WEBSITE FOR 
#WEATHER DATA AND CREATES A CSV FILE 

#THE PRINTS THAT ARE COMMENTED ARE MEANT TO DISPLAY THE PROCESS STEP BY STEP

# Get the page we want , find the element we want with id
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.0536&lon=-118.2454")
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast')


#Items list has all the temps and description for the week
items = week.find_all(class_='tombstone-container')


#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_= 'period-name').get_text() for item in items]
#print(period_names)
short_decc = [item.find(class_="short-desc").get_text() for item in items]
#print(short_decc)
temp =[item.find(class_="temp").get_text() for item in items]
#print(temp)

weather_stuff = pd.DataFrame(
    {
    'Period': period_names,
    'Short_description' : short_decc,
    'Tempratures' : temp,
    })

print(weather_stuff)

weather_stuff.to_csv("Weather Report LA")
