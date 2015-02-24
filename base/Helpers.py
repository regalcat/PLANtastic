from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

from base.events.models import EventModel

def getUser(request):
	return User(id=0)

def getEvent(event_id):
	return EventModel(eventid=event_id)

