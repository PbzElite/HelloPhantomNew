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
            print({self.text})
        except sr.UnknownValueError:
            print("what are you doing")

    def tts(self):
        #self.text = "Hello"
        language = "en"  # Specify the language (IETF language tag)
        output_file = "output.mp3"  # Specify the output file (only accepts .mp3)
        print({self.text})
        save(self.text, language, file=output_file)
    
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

        string = self.text
        words = string.split(' ')

        ##will make the keyword prompt as the word that's important that they found in the string that you said
        for i in range(len(words)):
            if words[i] == "weather" or words[i] == "temperature" or words[i] == "calendar" or words[i] == "events" or words[i] == "announcements":
                self.prompt = words[i]
                if words[i] == "calendar" or words[i] == "events" or words[i] == "event" or words[i] == "announcements":
                    if self.text.find("recent") != -1:
                        self.prompt += f" recent"
                break
            else:
                self.prompt = "not found"
        print(f"68 {self.prompt}")

        month = ""
        day = ""
        time = "" #don't know why it can't access, might be a local var issue and have to move it up
        
        #similar to line 59, but its the day not the keyward
        print(f"74 {string}")
        print(f"75 {words}")
        for i in range(len(words)):
            if words[i] == "yesterday" or words[i] == "today" or words[i] == "tomorrow":
                self.prompt += f" {words[i]}"
                dex = self.prompt.find(" ")
                if(self.prompt[dex:dex+5] == "today"):
                    self.date = datetime.date.today()
                if(self.prompt[dex:dex+9] == "yesterday"):
                    self.date = datetime.date.today() - datetime.timedelta(days=1)
                if(self.prompt[dex:dex+8] == "tomorrow"):
                    self.date = datetime.date.today() + datetime.timedelta(days=1)
                break
            elif words[i] == "January" or words[i] == "February" or words[i] == "March" or words[i] == "April" or words[i] == "May" or words[i] == "June" or words[i] == "July" or words[i] == "August" or words[i] == "September" or words[i] == "October" or words[i] == "November" or words[i] == "December":
                month = words[i]
                if words[i+1] == "1st" or words[i+1] == "2nd" or words[i+1] == "3rd" or words[i+1] == "4th" or words[i+1] == "5th" or words[i+1] == "6th" or words[i+1] == "7th" or words[i+1] == "8th" or words[i+1] == "9th" or words[i+1] == "10th" or words[i+1] == "11th" or words[i+1] == "12th" or words[i+1] == "13th" or words[i+1] == "14th" or words[i+1] == "15th" or words[i+1] == "16th" or words[i+1] == "17th" or words[i+1] == "18th" or words[i+1] == "19th" or words[i+1] == "20th" or words[i+1] == "21st" or words[i+1] == "22nd" or words[i+1] == "23rd" or words[i+1] == "24th" or words[i+1] == "25th" or words[i+1] == "26th" or words[i+1] == "27th" or words[i+1] == "28th" or words[i+1] == "29th" or words[i+1] == "30th" or words[i+1] == "31st":
                    day = words[i+1]
                    print(f"94 {month} {day}")

                    for i in range(len(monthArr)):
                        if month == monthArr[i]:
                            monthNum = i + 1
                    for i in range(len(dayArr)):
                        if day == dayArr[i]:
                            dayNum = i + 1
                    print(f"year {datetime.date.today().year} month {monthNum} day {dayNum}")
                    self.date = datetime.date(datetime.date.today().year, monthNum, dayNum)
                    print(self.date)
                break
            else:
                self.date = datetime.date.today()
        print(f"106 {self.prompt}")

        
    #converts event.date to datetime format
    import datetime

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
        # List of first three letters of each month
        short_months = [month[:3] for month in full_months]

        #Beautiful Soup
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')
        recentEvents = []

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
            # URL of the events page, this will need to be updated every year (scratch that cause it will cause huge delays)
            #format: https://bayportbluepointny.sites.thrillshare.com/events?start_date=2024-09-01&end_date=2025-10-31&filter_ids=327083,327083,325682,325682
            startdate = datetime.date.today() - datetime.timedelta(days=14)
            enddate = datetime.date.today() + datetime.timedelta(days=40)
            start = datetime.date(startdate.year,startdate.month,startdate.day)
            end = datetime.date(enddate.year,enddate.month,enddate.day)
            url = f"https://bayportbluepointny.sites.thrillshare.com/events?start_date={start}&end_date={end}&filter_ids=327083,327083,325682,325682"

            # Send a GET request to the webpage
            response = requests.get(url)

            # Check if the request was successful and see if the input is asking for events
            if response.status_code == 200:
                # Parse the HTML content of the page
                soup = BeautifulSoup(response.text, 'html.parser')

                # Find the container that holds the events
                events_container = soup.find_all('div', class_='event-list-item')  # Adjust the class based on the actual HTML structure
                
                # Iterate over each event and extract relevant details
                for event in events_container:
                    title = event.find('div', class_='title').text.strip() if event.find('div', class_='title') else 'No Title'
                    date = event.find('div', class_='month').text.strip() if event.find('div', class_='month') else 'No Date'
                    date += " " + event.find('div', class_='day').text.strip() if event.find('div', class_='day') else 'No Date'
                    time = event.find('div', class_='hour').text.strip() if event.find('div', class_='hour') else 'No Time'
                    location = event.find('div', class_='venue').text.strip() if event.find('div', class_='venue') else 'No Location'
                    #recentEvents.append(Event(str(title),str(date),str(time), str(location)))
                    recentEvents.append(Event(str(title),str(date), str(location)))
                
                #TASK: fix logic to get all commands working: maybe even lookup specific events (needs to be implemented)
                if(self.prompt.find("recent") != -1):
                    self.text = "current events include "
                    count = 0

                    for event in recentEvents:
                        for i in range(len(short_months)):
                            if(event.getDate()[:3] == short_months[i]):
                                num = int(event.getDate()[event.getDate().find(" ")+1:])
                                compDate = datetime.date(datetime.date.today().year,i+1,num)
                                if(count<3 and compDate >= datetime.date.today()):
                                    self.text += f"{event}"
                                    count+=1
                                break
                elif(self.prompt.find("tomorrow") != -1):
                    print(f"192 {self.date}")
                    self.text = "Tomorrows events are "
                    count = 0
                    
                    for event in recentEvents:
                        if(count <3):
                            for i in range(len(short_months)):
                                if(event.getDate()[:3] == short_months[i]):
                                    num = int(event.getDate()[event.getDate().find(" ")+1:])
                                    #compDate = datetime.date(datetime.date.today().year,i+1,num+1)
                                    cdate = datetime.date.today() + timedelta(days=1)
                                    compDate = datetime.date(cdate.year,cdate.month,cdate.day)
                                    #issue is the Sep 6 needs to be converted to 2024-09-06
                                    
                                    if(compDate == self.convert_string_to_date(str(event.getDate()))):
                                        self.text += f"{event}"
                                        print(f"201 {event}")
                                        count+=1
                                        break
                                    else:
                                        break
                        else:
                            break
                    if count == 0:
                        self.text = "There are no events on that day"
                elif(self.prompt.find("yesterday") != -1):
                    print(f"242 {self.date}")
                    self.text = "Yesterday's events were "
                    count = 0
                    
                    for event in recentEvents:
                        if(count <3):
                            for i in range(len(short_months)):
                                if(event.getDate()[:3] == short_months[i]):
                                    num = int(event.getDate()[event.getDate().find(" ")+1:])
                                    #compDate = datetime.date(datetime.date.today().year,i+1,num+1)
                                    cdate = datetime.date.today() - timedelta(days=1)
                                    compDate = datetime.date(cdate.year,cdate.month,cdate.day)
                                    #issue is the Sep 6 needs to be converted to 2024-09-06
                                    
                                    if(compDate == self.convert_string_to_date(str(event.getDate()))):
                                        self.text += f"{event}"
                                        print(f"201 {event}")
                                        count+=1
                                        break
                                    else:
                                        break
                        else:
                            break
                    if count == 0:
                        self.text = "There are no events on that day"
                elif(self.prompt.find("today") != -1):
                    self.text = "todays events include "
                    count = 0

                    for event in recentEvents:
                        for i in range(len(short_months)):
                            if(event.getDate()[:3] == short_months[i]):
                                num = int(event.getDate()[event.getDate().find(" ")+1:])
                                compDate = datetime.date(datetime.date.today().year,i+1,num)
                                if(count<3 and compDate == datetime.date.today()):
                                    self.text += f"{event}"
                                    count+=1
                                break
                    if count == 0:
                        self.text = "There are no events on today"
                else:
                    self.text = "The events on that day are "
                    count = 0

                    for event in recentEvents:
                        for i in range(len(short_months)):
                            if(event.getDate()[:3] == short_months[i]):
                                num = int(event.getDate()[event.getDate().find(" ")+1:])
                                datelook = datetime.date(2024,i+1,num)

                                compDate = self.date
                                if(count<3 and compDate == datelook):
                                    self.text += f"{event}"
                                    count += 1
                                break
                    if count == 0:
                        self.text = "There are no events on that day"
        else:
            response = requests.get(url)
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")