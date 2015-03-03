from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

from base.events.models import EventModel

# Returns the event that is currently in play from the event_id
def getEvent(event_id):
	return EventModel.objects.get(eventid=event_id)

def getUserEvents(user):
	#TODO - should access Invite Table
	return EventModel.objects.all()

def getMenuInfo(request):
	toReturn = {}
	toReturn['server'] = "http://" + request.get_host()
	# TODO - separate previous events from upcoming events
	toReturn['prev_events'] = getUserEvents(request.user)
	toReturn['upcoming_events'] = toReturn['prev_events']
	# TODO - Get Correct Options
	toReturn['event_types'] = ('Dinner', 'Hike')
	return toReturn
