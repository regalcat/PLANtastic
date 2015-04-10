from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone
from invite.models import MembershipModel


from events.models import EventModel


def getUserEvents(user_):
	membership_entries = MembershipModel.objects.filter(user=user_)
	events = []
	for entry in membership_entries:
		events.append(entry.event)
	return events

def isPreviousEvent(event_):
	today = timezone.now()
	return event_.eventDateStart < today

def getPreviousEvents(user_):
	membership_entries = MembershipModel.objects.filter(user=user_)
	events = []
	for entry in membership_entries:
		today = timezone.now()
		if entry.event.eventDateStart < today:
			events.append(entry.event)
	
	return events

def getUpcomingEvents(user_):
	membership_entries = MembershipModel.objects.filter(user=user_)
	events = []
	today = timezone.now()
	for entry in membership_entries:
		if entry.event.eventDateStart >= today:
			events.append(entry.event)

	return events

def getMenuInfo(request):
	toReturn = {}
	toReturn['server'] = "http://" + request.get_host()
	toReturn['prev_events'] = getPreviousEvents(request.user)
	toReturn['upcoming_events'] = getUpcomingEvents(request.user)
	toReturn['event_types'] = EventModel.getEventTypes()
	return toReturn
