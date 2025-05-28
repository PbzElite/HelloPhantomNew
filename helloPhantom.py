import speech_recognition as sr
from text_to_speech import save
import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import datetime
from helloPhantom import *
from Events import *
import pandas as pd
from OllamaCalling import *


class HelloPhantom:
    #, prompt, date, text
    def __init__(self):
        self.prompt = ""
        self.date = ""
        #self.text = "january first"
        self.text = ""
        self.month = ""
        self.day = ""

    def getPrompt(self):
        return self.prompt

    #speech to text
    def stt(self):
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Say something!")
            audio = r.listen(source)
            
        try:
            self.text = r.recognize_google(audio,language="en")
            print({self.text})
        except sr.UnknownValueError:
            print("what are you doing")

    #text to speech
    def tts(self):
        #self.text = "Hello"
        language = "en"  # Specify the language (IETF language tag)
        output_file = "output.mp3"  # Specify the output file (only accepts .mp3)
        print({self.text})
        save(self.text, language, file=output_file)
    
    month = ""
    day = ""
    time = "" #don't know why it can't access, might be a local var issue and have to move it up
    
    #sets the prompt to the specific keywords
    def recognizer(self):
        #simplified code for the month and day system
        monthArr = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        dayArr = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', 
 '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', 
 '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', 
 '29th', '30th', '31st']

        monthNum = -1
        dayNum = -1

        api = OllamaCalling()
        string = api.generate(self.text)
        words = string.split(' ')
        #self.trimWords(words)

        ##will make the keyword prompt as the word that's important that they found in the string that you said
        for i in range(len(words)):
            if words[i] == "weather" or words[i] == "temperature" or words[i] == "Weather" or words[i] == "calendar" or words[i] == "events" or words[i] == "announcements" or words[i] == "Events" or words[i] == "intent:events":
                self.prompt = words[i]
                if words[i] == "calendar" or words[i] == "events" or words[i] == "event" or words[i] == "announcements":
                    if self.text.find("recent") != -1:
                        self.prompt += f" recent"
                break
            #else:
                #self.prompt = "not found"
        print(f"68 {self.prompt}")

        
        #similar to line 59, but its the day not the keyward
        print(f"74 {string}")
        print(f"75 {words}")
        for i in range(len(words)):
            if words[i].find("yesterday") != -1 or words[i].find("today") != -1 or words[i].find("tomorrow") != -1:
                self.prompt += f" {words[i]}"
                dex = self.prompt.find(" ")
                if(self.prompt[dex+1:dex+6] == "today"):
                    self.date = datetime.date.today()
                    self.day = str(self.date.day) + "xx"
                    self.month = monthArr[self.date.month - 1]
                if(self.prompt[dex+1:dex+10] == "yesterday"):
                    self.date = datetime.date.today() - datetime.timedelta(days=1)
                    self.day = str(self.date.day) + "xx"
                    self.month = monthArr[self.date.month - 1]
                if(self.prompt[dex+1:dex+9] == "tomorrow"):
                    self.date = datetime.date.today() + datetime.timedelta(days=1)
                    self.day = str(self.date.day) + "xx"
                    self.month = monthArr[self.date.month - 1]
                break
            elif words[i] == "January" or words[i] == "February" or words[i] == "March" or words[i] == "April" or words[i] == "May" or words[i] == "June" or words[i] == "July" or words[i] == "August" or words[i] == "September" or words[i] == "October" or words[i] == "November" or words[i] == "December":
                self.month = words[i] #put first three letters if need
                if words[i+1] == "1st" or words[i+1] == "2nd" or words[i+1] == "3rd" or words[i+1] == "4th" or words[i+1] == "5th" or words[i+1] == "6th" or words[i+1] == "7th" or words[i+1] == "8th" or words[i+1] == "9th" or words[i+1] == "10th" or words[i+1] == "11th" or words[i+1] == "12th" or words[i+1] == "13th" or words[i+1] == "14th" or words[i+1] == "15th" or words[i+1] == "16th" or words[i+1] == "17th" or words[i+1] == "18th" or words[i+1] == "19th" or words[i+1] == "20th" or words[i+1] == "21st" or words[i+1] == "22nd" or words[i+1] == "23rd" or words[i+1] == "24th" or words[i+1] == "25th" or words[i+1] == "26th" or words[i+1] == "27th" or words[i+1] == "28th" or words[i+1] == "29th" or words[i+1] == "30th" or words[i+1] == "31st":
                    self.day = words[i+1]
                    print(f"94 {self.month} {self.day}")

                    for i in range(len(monthArr)):
                        if self.month == monthArr[i]:
                            monthNum = i + 1
                    for i in range(len(dayArr)):
                        if self.day == dayArr[i]:
                            dayNum = i + 1
                    print(f"year {datetime.date.today().year} month {monthNum} day {dayNum}")
                    self.date = datetime.date(datetime.date.today().year, monthNum, dayNum)
                break
            else:
                self.date = datetime.date.today()
        print(f"106 {self.prompt}")
        
    #converts event.date to datetime format
    def convert_string_to_date(self,date_str, year=2024):
        # Check if date_str is a string
        #if not isinstance(date_str, str):
            #raise TypeError(f"Expected a string for date_str, but got {type(date_str).__name__}")
        
        # Convert the date_str argument to a datetime object
        #try:
        date_obj = datetime.datetime.strptime(date_str, "%b %d")
        #except ValueError as e:
           # raise ValueError(f"Invalid date format: {date_str}. Expected format: 'Sep 6'.") from e
        
        # Create a datetime.date object using the year, month, and day
        full_date = datetime.date(year, date_obj.month, date_obj.day)
        return full_date

    #trim the start of the words, used when ollama kept putting its statement format weird, now not needed
    def trimWords(self,arr):
        for i in range(len(arr)):
            while arr[i].find(":") != -1:
                arr[i] = arr[i][arr[i].find(":")+1:]
        print(f"pre {arr}")

    #sets what the bot will speak based on the keywords
    def process(self):
        url = "https://www.wunderground.com/weather/us/ny/bayport/"
        #0000-00-00
        start = self.prompt.find(" ")
        input = f"{self.date}"
        today = datetime.date.today()
        tomorrow = today + timedelta(days=1)

        if input != str(today):
            url = f"https://www.wunderground.com/hourly/us/ny/bayport/KISP/date/{input}"

        #month arrars, later used
        full_months = ["January", "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"]
        
        #Beautiful Soup
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')
        
        if self.prompt.find("weather") != -1 and str(self.date) == str(today):
            temperature = soup.find('div', attrs={'class': 'current-temp'}).text.strip() #tried to make it say not found if it isnt but it don't work, if soup.find('div', attrs={'class': 'current-temp'}).text.find("--") != -1 else  "not found"
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
        elif self.prompt.find("weather") != -1 and str(self.date) != str(tomorrow):
            next = soup.findAll('div', attrs={'class': 'hook'})
            next = next[0]
            print(f"{next}")
        #prints the events output
        elif self.prompt.find("events") != -1 or self.prompt.find("event") != -1 or self.prompt.find("announcements") != -1:
            eS = pd.read_excel('BBP_March_2025_Events.xlsx')
        
            #TASK: fix logic to get all commands working: today (good),recent (needs checking),yesterday (good) ,tomorrow ( good),specific date (needs to be implemented), maybe even lookup specific events (needs to be implemented)
            if self.prompt.find("recent") != -1 or self.prompt.find("today") != -1 or self.prompt.find("tomorrow") != -1 or self.prompt.find("yesterday") != -1:
                self.text = "There is a "
                count = 0
                print(f"225 {self.month[:3]} {self.day[:-2]}")

                for index, row in eS.iterrows():
                    if str(row["Date"]).strip() == (f"{self.month[:3]} {self.day[:-2]}"):
                        if count != 0:
                            self.text += " and "
                        self.text += str(eS['Title'].iloc[index])
                        count += 1
                if count == 0:
                    self.text = "There are no events"
            else:
                self.text = "There is a "
                count = 0   
                for index, row in eS.iterrows():
                    if str(row["Date"]).strip() == (f"{self.month[:3]} {self.day[:-2]}"):
                        if count > 0:
                            self.text += " and "
                        self.text += str(eS['Title'].iloc[index])
                        count += 1