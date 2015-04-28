#imported from django and/or python
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.templatetags.static import static
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout, update_session_auth_hash
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password, is_password_usable
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from base.permissions import getMemberObject

from os import listdir
from os.path import isfile, join

#imported from our project

from models import EventModel, HikeEventModel, DinnerEventModel, GenericTripModel, GenericGatheringModel
from invite.models import InviteModel, MembershipModel
from users.forms import UserRegistrationForm
from base.helpers import getMenuInfo, isPreviousEvent
from base.permissions import memberCheck, isCreator, isCoplanner
from forms import EventForm, HikeForm, GenericTripForm, GenericGatheringForm, DinnerForm
from notifications.models import NotificationModel


@login_required(login_url = '/loginRequired/')
def upcoming(request):
	return render(request, 'events/upcoming.html', {'menu' : getMenuInfo(request), 'title' : "Upcoming Events"})

@login_required(login_url = '/loginRequired/')
def past(request):
	
	return render(request, 'events/past.html', { 'menu' : getMenuInfo(request), 'title' : "Past Events"})

@login_required(login_url = '/loginRequired/')
def editEvent(request, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	if memberCheck(request.user, event[0]) == False:
		return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : 'Not Member'})
	creator = isCreator(request.user, event[0])
	coplanner = isCoplanner(request.user, event[0])
	if creator == False:
		if coplanner == False:
			return render(request, 'events/notPermission.html', \
			{'menu' : getMenuInfo(request), 'title' : 'Not Permission'})
	
	
	event = EventModel.getEvent(eventid)

	if request.method == 'GET':
		editeventform = EventForm(instance = event)
		context = {'menu' : getMenuInfo(request), 'title' : 'Edit Event', \
			'editeventform' : editeventform, 'event' : event, 'creator' : creator, 'coplanner' : coplanner}

		if isPreviousEvent(event):
			context['previous'] = True
		else:
			context['upcoming'] = True

		if event.eventType == u'hike':
			subform = HikeForm(instance = event)
			
		elif event.eventType == u'otherTrip':
			subform = GenericTripForm(instance = event)

		elif event.eventType == u'otherGathering':
			subform = GenericGatheringForm(instance = event)

		elif event.eventType == u'dinner':
			subform = DinnerForm(instance = event)

		context['subform'] = subform
		
		return render(request, 'events/editEvent.html', context)
		
	if request.method == 'POST':
		editeventform = EventForm(request.POST, instance = event)

		if editeventform.is_valid():
			if event.eventType == u'hike':
				subform = HikeForm(request.POST, instance = event)
				
			elif event.eventType == u'otherTrip':
				subform = GenericTripForm(request.POST, instance = event)
				
			elif event.eventType == u'otherGathering':
				subform = GenericGatheringForm(request.POST, instance = event)
				
			elif event.eventType == u'dinner':
				subform = DinnerForm(request.POST, instance = event)

			if subform.is_valid():
					editeventform.save(commit = False)
					editeventform.creator = request.user
					editeventform.save()
					subform.save()

		return HttpResponseRedirect("")




@login_required(login_url = '/loginRequired/')
def editMembers(request, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	if memberCheck(request.user, event[0]) == False:
		return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : 'Not Member'})
	if isCreator(request.user, event[0]) == False:
		return render(request, 'events/notPermission.html', {'menu' : getMenuInfo(request), 'title' : 'Not Permission'})

	event = EventModel.getEvent(eventid)
	members = MembershipModel.objects.filter(event = event)
		

	if request.method == 'GET':
		return render(request, 'events/editMembers.html', { 'menu' : getMenuInfo(request), 'title' : "Edit Members", 'event' : event, 'members' : members})

	if request.method == "POST":
		username = request.POST['user']
		status = request.POST['status']
		user = User.objects.filter(username = username)
		event = EventModel.objects.filter(eventid = eventid)
		member = getMemberObject(user, event)
		member.status = status
		member.save()

		note = NotificationModel()
		text = "Your status in the event " + str(event[0].name) + " just got changed to " + str(member.get_status_display) + "."
		note.createNewNotification(member.user, text)		

		return HttpResponseRedirect("")	

@login_required(login_url = '/loginRequired/')
def deleteMember(request, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	if memberCheck(request.user, event[0]) == False:
		return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : 'Not Member'})
	if isCreator(request.user, event[0]) == False:
		return render(request, 'events/notPermission.html', {'menu' : getMenuInfo(request), 'title' : 'Not Permission'})

	username = request.POST['user']
	

	return render(request, 'events/deleteMember.html', { 'menu' : getMenuInfo(request), 'title' : "Leave Event", 'event' : event[0], 'username':username})


@login_required(login_url = '/loginRequired/')
def executeDeleteMember(request, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	if memberCheck(request.user, event[0]) == False:
		return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : 'Not Member'})
	if isCreator(request.user, event[0]) == False:
		return render(request, 'events/notPermission.html', {'menu' : getMenuInfo(request), 'title' : 'Not Permission'})

	username = request.POST['username']
	event = EventModel.getEvent(eventid)

	user = User.objects.filter(username = username)
	event = EventModel.objects.filter(eventid = eventid)
	member = getMemberObject(user[0], event[0])

	note = NotificationModel()
	text = "You are no longer a member of the event " + str(event[0].name) + "."
	note.createNewNotification(user=user[0], text=text)

	member.delete()

	return HttpResponseRedirect(reverse('events:editMembers', kwargs={'eventid':eventid}))	

@login_required(login_url = '/loginRequired/')
def leaveEvent(request, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	if memberCheck(request.user, event[0]) == False:
		return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : 'Not Member'})
	if isCreator(request.user, event[0]) == True:
		return render(request, 'events/notPermission.html', {'menu' : getMenuInfo(request), 'title' : 'Not Permission'})
	

	return render(request, 'events/leaveEvent.html', { 'menu' : getMenuInfo(request), 'title' : "Leave Event", 'event' : event[0]})



@login_required(login_url = '/loginRequired/')
def executeLeaveEvent(request, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	if memberCheck(request.user, event[0]) == False:
		return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : 'Not Member'})
	if isCreator(request.user, event[0]) == True:
		return render(request, 'events/notPermission.html', {'menu' : getMenuInfo(request), 'title' : 'Not Permission'})

	creator = MembershipModel.objects.filter(event=event[0], status = "CR")
	notifications = NotificationModel()
	text = str(request.user.username) + " has just left your event " + str(event[0].name) + "."
	notifications = notifications.createNewNotification(user=creator[0].user, text = text)

	event = EventModel.objects.filter(eventid = eventid)
	member = getMemberObject(request.user, event)
	member.delete()

	return HttpResponseRedirect(reverse('base:upcoming'))
	


@login_required(login_url = '/loginRequired/')
def deleteEvent(request, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	if memberCheck(request.user, event[0]) == False:
		return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : 'Not Member'})
	if isCreator(request.user, event[0]) == False:
		return render(request, 'events/notPermission.html', {'menu' : getMenuInfo(request), 'title' : 'Not Permission'})
	event = EventModel.getEvent(eventid)

	context = {'menu' : getMenuInfo(request), 'title' : 'Delete Event', 'event':event}
	return render(request, "events/deleteEvent.html", context)


@login_required(login_url = '/loginRequired/')
def executeDeleteEvent(request, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	if memberCheck(request.user, event[0]) == False:
		return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : 'Not Member'})
	if isCreator(request.user, event[0]) == False:
		return render(request, 'events/notPermission.html', {'menu' : getMenuInfo(request), 'title' : 'Not Permission'})
	
	text = "The event " + str(event[0].name) + " that you were a member of has been deleted by the creator."

	members = MembershipModel.objects.filter(event=event[0])
	for member in members:
		note = NotificationModel()
		note.createNewNotification(user = member.user, text = text)
			

	eventChild = EventModel.getEvent(eventid)
	eventChild.delete()
	event.delete()

	return HttpResponseRedirect(reverse('base:upcoming'))

@login_required(login_url = '/loginRequired/')  # User have to be logged in to see this view - if not: redirects to loginRequired
def submit_new(request):
	if request.method == "POST":
		eventform = EventForm(request.POST)
		if eventform.is_valid():
			eventform.save()
			return HttpResponseRedirect(reverse('base:eventHome'))
	return HttpResponseRedirect(reverse('base:new_event'))
