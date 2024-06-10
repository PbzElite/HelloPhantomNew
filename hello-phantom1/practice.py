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

#used to be here, now in the process method of HelloPhantom
'''
if BBP.getPrompt() == "weather":
    #if the date of the input is not today, the "api" reads the weather for whatever the date is
    if input != str(today) and input != str(today):
        url = f"https://www.wunderground.com/hourly/us/ny/bayport/KISP/date/{input}"
        #print("ran1")

    #Beautifulsoup
    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')

    # print(soup.prettify())

    #if the input IS today, then the temperature, high and low, and a blurb is found
    #prints the weather output
    if input == str(today):
        temperature = soup.find('div', attrs={'class': 'current-temp'}).text #tried to make it say not found if it isnt but it don't work, if soup.find('div', attrs={'class': 'current-temp'}).text.find("--") != -1 else  "not found"
        hilo = soup.find('div', attrs={'class': 'hi-lo'}).text
        blurb = soup.findAll('div', attrs={'class': 'columns small-6 medium-12'})

        blurb = blurb[1].text
        #print(blurb)
        percent, amount, high, wind = blurb.split(". ", 3)
        percent = percent.split(" ")
        amount = amount.split("°")
        wind = wind[0].lower() + wind[1:]
        hilo = hilo.split(" | ")

        print(f"The current temperature is {temperature}. The high is {hilo[0]} and the low is {hilo[1]}. The chance of rain is {percent[0]}. The amount of rain today is {amount[0].replace('/ ', '').strip()} inches. Current {wind.replace('winds ', 'winds are ')} ")
        #print("ran2")
    elif input == str(tomorrow):
        next = soup.findAll('div', attrs={'class': 'hook'})
        next = next[0]
        print(f"{next}")
        #print("ran3")
#prints the events output
#have to make it print recents, on a specific date, or something, HAVE TO base on the prompt
elif BBP.getPrompt() == "events" or BBP.getPrompt() == "announcements":
    #Added the events of a calendar, requires some tweaking
    # URL of the events page
    url = "https://www.bbpschools.org/o/bbphs/events"
    input = "What are the recent events"

    # Send a GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful and see if the input is asking for events
    if input.find("event") != -1 and response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the container that holds the events
        events_container = soup.find_all('div', class_='event-list-item')  # Adjust the class based on the actual HTML structure
        
        #calendar event class
        class Event:
            #acts as a constructor
            def __init__(self,title,date,time,location):
                self.title = title
                self.date = date
                self.time = time
                self.location = location
            
            #purely aesthetic accesssor methods
            def getTitle(self):
                return self.title
            def getDate (self):
                return self.date
            def getTime(self):
                return self.time
            def getLocation(self):
                return self.location
            
            #this is what is returned when you try to print an object of this class
            def __str__(self):
                return f"- {self.title} on {self.date} at {self.time} at {self.location}"

        #list of events in this, showing that you cant create on the fly
        recentEvents = [Event("ohio","jun 9","6:30","BBPHS"),Event("detroit","may 20","4:20","chillicothe")]

        #listing the elements of recentEvents
        print("Current events include:")
        for event in recentEvents:
            print(event)
    
        print("-"*40)
        # Iterate over each event and extract relevant details
        for event in events_container[:3]:
            title = event.find('div', class_='title').text.strip() if event.find('div', class_='title') else 'No Title'
            date = event.find('div', class_='month').text.strip() if event.find('div', class_='month') else 'No Date'
            date += " " + event.find('div', class_='day').text.strip() if event.find('div', class_='day') else 'No Date'
            time = event.find('div', class_='hour').text.strip() if event.find('div', class_='hour') else 'No Time'
            location = event.find('div', class_='venue').text.strip() if event.find('div', class_='venue') else 'No Location'

            #make a class for event

            # Print the extracted details
            print(f"Title: {title}")
            print(f"Date: {date}")
            print(f"Time: {time}")
            print(f"Location: {location}") if location.strip() != "" else print("")
            print("-" * 40)
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    #for event in recentEvents:
        #print(f"Current events include:" {title} "on " {date} "at " {time})
'''
#print("done")