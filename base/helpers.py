from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone
from invite.models import MembershipModel
import datetime

from events.models import EventModel

def getUserEvents(user_):
	membership_entries = MembershipModel.objects.filter(user=user_)
	events = []
	for entry in membership_entries:
		events.append(entry.event)
	return events

def isPreviousEvent(event_):
	today = timezone.now().date()
	#today = datetime.datetime.now().date()
	if event_.eventDateStart == None:
		return True
	return event_.eventDateStart < today

def isUpcomingEvent(event_):
	today = timezone.now().date()
	#today = datetime.today.date()
	if event_.eventDateStart == None:
		return True
	
	#subevent = event_.getEvent(event_.eventid)
	#if subevent.eventDateEnd:
	#	return subevent.eventDateEnd >= today

	return event_.eventDateStart >= today

def getPreviousEvents(user_):
	membership_entries = MembershipModel.objects.filter(user=user_)
	events = []
	for entry in membership_entries:
		if isPreviousEvent(entry.event):
			events.append(entry.event)
	
	return events

def getUpcomingEvents(user_):
	membership_entries = MembershipModel.objects.filter(user=user_)
	events = []
	today = timezone.now()
	for entry in membership_entries:
		if isUpcomingEvent(entry.event):
			events.append(entry.event)

	return events

def getMenuInfo(request):
	toReturn = {}
	toReturn['server'] = "http://" + request.get_host()
	toReturn['prev_events'] = getPreviousEvents(request.user)
	toReturn['upcoming_events'] = getUpcomingEvents(request.user)
	toReturn['event_types'] = EventModel.getEventTypes()
	return toReturn
