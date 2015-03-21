from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

from base.events import models as event_models

# Returns the event that is currently in play from the event_id
def getEvent(event_id):
	events = event_models.HikeEventModel.objects.filter(eventid=event_id)
	if (events.count() == 1):
		return events[0]
	events = event_models.GenericTripModel.objects.filter(eventid=event_id)
	if (events.count == 1):
		return events[0]
	events = event_models.GenericGatheringModel.objects.filter(eventid=event_id)
	if events.count == 1:
		return events[0]
	return event_models.EventModel.objects.get(eventid=event_id)

def getUserEvents(user):
	#TODO - should access Invite Table
	return event_models.EventModel.objects.all()

def getMenuInfo(request):
	toReturn = {}
	toReturn['server'] = "http://" + request.get_host()
	# TODO - separate previous events from upcoming events
	toReturn['prev_events'] = getUserEvents(request.user)
	toReturn['upcoming_events'] = toReturn['prev_events']
	toReturn['event_types'] = event_models.EventModel.getEventTypes()
	return toReturn
