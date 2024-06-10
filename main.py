import requests
from bs4 import BeautifulSoup

#COPY HERE
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
    #print(events_container)

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

        # Print the extracted details
        print(f"Title: {title}")
        print(f"Date: {date}")
        print(f"Time: {time}")
        print(f"Location: {location}") if location.strip() != "" else print("BBPHS")
        print("-" * 40)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")