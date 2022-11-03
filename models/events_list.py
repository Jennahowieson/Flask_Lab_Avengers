from models.event import Event
import datetime

# event1 = Event(date,name,guest_number,location,description,recurring)

event1 = Event(datetime.datetime(2022, 11, 3, 14, 30),
    "Robotics",
    20,
    "Stark Tower",
    "Learn to build your first robot with Tony Stark",
    False)
#2022-11-11T18:00
event2 = Event(datetime.datetime(2022, 11, 3, 16, 30),
    "Weapons Forging",
    30,
    "Asgard",
    "Construct your weapons with Thor",
    False)

events = [event1, event2]

def add_new_event(new_event):
    events.append(new_event)