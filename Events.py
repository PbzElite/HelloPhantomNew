import datetime

class Event:
    #acts as a constructor
    def __init__(self,title,date,time,location):
        self.title = title
        self.date = date
        self.time = time
        self.location = location
                    
    def __init__(self,title,date,location):
        self.title = title
        self.date = date
        self.time = None
        self.location = location

    #purely aesthetic accesssor methods
    def getTitle(self):
        return self.title
    def getDate (self):
        return self.date
    def setDate(self,str):
        self.date = str
    def getTime(self):
        return self.time
    def getLocation(self):
        return self.location

    #this is what is returned when you try to print an object of this class
    def __str__(self):
        # return f"{self.title} on {self.date} at {self.time} at {self.location}"
        #TASK: look to see if you can remove: HS or BP or etc. at start of self.title
        return f"{self.title} on {self.date}. "
