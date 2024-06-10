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
        return f"{self.title} on {self.date} at {self.time} at {self.location}"
