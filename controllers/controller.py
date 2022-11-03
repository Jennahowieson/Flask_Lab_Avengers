from app import app
from flask import render_template, request
from models import events_list
from models.event import Event
import datetime

@app.route('/events')
def events():
    return render_template('events.html', events = events_list.events)

@app.route('/events', methods=['POST'])
def add_event():
    event_date = request.form['date']
    print("the time is a: " + str(type(event_date)))
    event_name = request.form['title']
    event_capacity = request.form['capacity']
    event_location = request.form['location']
    event_description = request.form['description']
    event_recurring = request.form['recurring']
    if event_recurring == "on":
        event_recurring = True
    else:
        event_recurring = False
    new_event = Event(datetime.datetime.strptime(event_date, "%Y-%m-%dT%H:%M"),event_name,event_capacity,
    event_location,event_description,event_recurring)
    events_list.add_new_event(new_event)
    return render_template('events.html', events = events_list.events)