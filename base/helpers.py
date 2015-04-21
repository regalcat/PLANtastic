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
	today = timezone.now().date()
	if event_.event_Start_Date == None:
		return True

	subevent = event_.getEvent(event_.eventid)
	if (subevent.eventType != u'dinner'):
	
		if subevent.event_End_Date != None:
			return subevent.event_End_Date < today
		return event_.event_Start_Date < today
	return event_.event_Start_Date < today

def isUpcomingEvent(event_):
	today = timezone.now().date()
	if event_.event_Start_Date == None:
		return True
	
	subevent = event_.getEvent(event_.eventid)
	if subevent.eventType != u'dinner':
		if subevent.event_End_Date:
			return subevent.event_End_Date >= today

	return event_.event_Start_Date >= today

def getPreviousEvents(user_):
	membership_entries = MembershipModel.objects.filter(user=user_)
	events = []
	for entry in membership_entries:
		if isPreviousEvent(entry.event):
			events.append(entry.event)
	
	return events

#def getFeaturedPrevEvent(user_):
	

#def getFeaturedUpcomingEvent(user_):

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
	toReturn['num_prev_events'] = len(getPreviousEvents(request.user))
	toReturn['num_upcoming_events'] = len(getUpcomingEvents(request.user))
	toReturn['event_types'] = EventModel.getEventTypes()
	return toReturn
