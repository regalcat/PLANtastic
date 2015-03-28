from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

from base.events import models as event_models
from base.invite.models import MembershipModel

def getUserEvents(user_):
	membership_entries = MembershipModel.objects.filter(user=user_)
	events = []
	for entry in membership_entries:
		events.append(entry.event)
	return events

def getMenuInfo(request):
	toReturn = {}
	toReturn['server'] = "http://" + request.get_host()
	# TODO - separate previous events from upcoming events
	toReturn['prev_events'] = getUserEvents(request.user)
	toReturn['upcoming_events'] = toReturn['prev_events']
	toReturn['event_types'] = event_models.EventModel.getEventTypes()
	return toReturn
