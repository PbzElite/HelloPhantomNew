import speech_recognition as sr
from text_to_speech import save
import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import datetime
from helloPhantom import *
from Events import *

class HelloPhantom:
    
    #, prompt, date, text
    def __init__(self):
        self.prompt = ""
        self.date = ""
        #self.text = "january first"
        self.text = ""

    def getPrompt(self):
        return self.prompt

    #put self in the parentheses if this don't work, I haven't checked
    def stt(self):
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Say something!")
            audio = r.listen(source)
            
        try:
            self.text = r.recognize_google(audio,language="en")
        except sr.UnknownValueError:
            print("what are you doing")

    def tts(self):
        #self.text = "Hello"
        language = "en"  # Specify the language (IETF language tag)
        output_file = "output.mp3"  # Specify the output file (only accepts .mp3)

        save(self.text, language, file=output_file)
    
    #sets the prompt to the specific keywords
    def recognizer(self):
        string = self.text
        words = string.split(' ')

        for i in range(len(words)):
            if words[i] == "weather" or words[i] == "temperature" or words[i] == "calendar" or words[i] == "events" or words[i] == "announcements":
                self.prompt = words[i]
                break
            else:
                self.prompt = "not found"
        print(self.prompt)

        month = ""
        day = ""
        time = "" #don't know why it can't access, might be a local var issue and have to move it up

        for i in range(len(words)):
            if words[i] == "yesterday" or words[i] == "today" or words[i] == "tomorrow":
                time = words[i]
                break
            elif words[i] == "january" or words[i] == "february" or words[i] == "march" or words[i] == "april" or words[i] == "may" or words[i] == "june" or words[i] == "july" or words[i] == "august" or words[i] == "september" or words[i] == "october" or words[i] == "november" or words[i] == "december":
                month = words[i]
                if words[i+1] == "first" or words[i+1] == "second" or words[i+1] == "third" or words[i+1] == "fourth" or words[i+1] == "fifth" or words[i+1] == "sixth" or words[i+1] == "seventh" or words[i+1] == "eighth" or words[i+1] == "ninth" or words[i+1] == "tenth" or words[i+1] == "eleventh" or words[i+1] == "twelfth" or words[i+1] == "thirteenth" or words[i+1] == "fourteenth" or words[i+1] == "fifteenth" or words[i+1] == "sixteenth" or words[i+1] == "seventeenth" or words[i+1] == "eighteenth" or words[i+1] == "nineteenth" or words[i+1] == "twentieth" or words[i+1] == "twenty-first" or words[i+1] == "twenty-second" or words[i+1] == "twenty-third" or words[i+1] == "twenty-fourth" or words[i+1] == "twenty-fifth" or words[i+1] == "twenty-sixth" or words[i+1] == "twenty-seventh" or words[i+1] == "twenty-eighth" or words[i+1] == "twenty-ninth" or words[i+1] == "thirtieth" or words[i+1] == "thirty-first":
                    day = words[i+1]
                    break
            else:
                self.date = datetime.date.today()
            
            #simplified code for the month and day system
            monthArr = ["january","february","march","april","may","june","july","august","september","october","november","december"]
            dayArr = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 
                    'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 
                    'eighteen', 'nineteen', 'twenty', 'twenty-one', 'twenty-two', 'twenty-three', 
                    'twenty-four', 'twenty-five', 'twenty-six', 'twenty-seven', 'twenty-eight', 
                    'twenty-nine', 'thirty', 'thirty-one']
            monthNum = -1
            dayNum = -1
            
            for i in range(len(monthArr)):
                if month == monthArr[i]:
                    monthNum = i + 1
 
            for i in range(len(dayArr)):
                if day == dayArr[i]:
                    dayNum = i + 1
            
            current = datetime.date.today() 
            self.date = (current.year, monthNum, dayNum)
                
            if time == "today":
                self.date = datetime.date.today()
            elif time == "yesterday":
                self.date = datetime.date.today() - datetime.timedelta(days=1)
            elif time == "tomorrow":
                self.date = datetime.date.today() + datetime.timedelta(days=1)
        self.prompt += f" {d.isoformat(self.date)}" 
    
    #sets what the bot will speak based on the keywords
    def process(self):
        
        url = "https://www.wunderground.com/weather/us/ny/bayport/"
        #0000-00-00
        #how to change this input based on the prompt, thinking to do something in this format: "keyword date" so it can just substring it
        input = f"{self.prompt[self.prompt.find(" "):self.prompt.find(" ")+10]}"
        today = datetime.date.today()
        tomorrow = today + timedelta(days=1)

        #month arrars, later used
        full_months = ["January", "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"]
        # List of first three letters of each month
        short_months = [month[:3] for month in full_months]

        #Beautiful Soup
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')
        recentEvents = []

        #if the input IS today, then the temperature, high and low, and a blurb is found
        #prints the weather output
        if self.prompt.find("weather") != -1 and input == str(today):
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
            self.text = f"The current temperature is {temperature}. The high is {hilo[0]} and the low is {hilo[1]}. The chance of rain is {percent[0]}. The amount of rain today is {amount[0].replace('/ ', '').strip()} inches. Current {wind.replace('winds ', 'winds are ')} "
            #print("ran2")
        elif input == str(tomorrow):
            next = soup.findAll('div', attrs={'class': 'hook'})
            next = next[0]
            print(f"{next}")
            #print("ran3")
        #prints the events output
        elif self.prompt == "events" or self.prompt() == "announcements":
            #Added the events of a calendar, requires some tweaking
            # URL of the events page
            url = "https://www.bbpschools.org/o/bbphs/events"
            #input = "What are the recent events"

            # Send a GET request to the webpage
            response = requests.get(url)

            # Check if the request was successful and see if the input is asking for events
            if self.prompt.find("events") != -1 or self.prompt.find("event") != -1 and response.status_code == 200:
                # Parse the HTML content of the page
                soup = BeautifulSoup(response.text, 'html.parser')

                # Find the container that holds the events
                events_container = soup.find_all('div', class_='event-list-item')  # Adjust the class based on the actual HTML structure
                
            # Iterate over each event and extract relevant details
            for event in events_container[:3]:
                title = event.find('div', class_='title').text.strip() if event.find('div', class_='title') else 'No Title'
                date = event.find('div', class_='month').text.strip() if event.find('div', class_='month') else 'No Date'
                date += " " + event.find('div', class_='day').text.strip() if event.find('div', class_='day') else 'No Date'
                time = event.find('div', class_='hour').text.strip() if event.find('div', class_='hour') else 'No Time'
                location = event.find('div', class_='venue').text.strip() if event.find('div', class_='venue') else 'No Location'
                recentEvents.append(Event(str(title),str(date),str(time),str(location)))

                # Print the extracted details
                '''
                print(f"Title: {title}")
                print(f"Date: {date}")
                print(f"Time: {time}")
                print(f"Location: {location}") if location.strip() != "" else print("")
                print("-" * 40)
                '''
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        self.text = "current events include "
        for event in recentEvents:
            #print(event)
            self.text += f"{event} and "
