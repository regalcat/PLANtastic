from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

from base.events.models import EventModel

# Returns the user that is currently logged in
def getUser(request):
	# TODO
	return User.objects.filter(id=1)[0]

# Returns the event that is currently in play from the event_id
def getEvent(event_id):
	return EventModel(eventid=event_id)

def getUserEvents(user):
	#TODO - should access Invite Table
	return EventModel.objects.all()

def getMenuInfo(request):
	toReturn = {}
	toReturn['user'] = getUser(request)
	toReturn['server'] = "http://" + request.get_host()
	# TODO - separate previous events from upcoming events
	toReturn['prev_events'] = getUserEvents(toReturn['user'])
	toReturn['upcoming_events'] = toReturn['prev_events']
	# TODO - Get Correct Options
	toReturn['event_types'] = ('Dinner', 'Hike')
	return toReturn
