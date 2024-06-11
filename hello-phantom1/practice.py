import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
from helloPhantom import *
from Events import *

url = "https://www.wunderground.com/weather/us/ny/bayport/"

input = "2024-06-09"
today = date.today()
tomorrow = today + timedelta(days=1)

#month arrars, later used
full_months = ["January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"]
# List of first three letters of each month
short_months = [month[:3] for month in full_months]

BBP = HelloPhantom()
BBP.stt()
BBP.recognizer()
BBP.process()
BBP.tts()