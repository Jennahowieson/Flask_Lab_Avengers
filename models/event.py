class Event:
    def __init__(self,date,name,capacity,location,description,recurring):
        self.date = date
        self.name = name 
        self.capacity = capacity
        self.location = location 
        self.description = description
        self.recurring = recurring

    def return_date_string(self):
        return self.date.strftime("%A %d %b %y at %H:%M")