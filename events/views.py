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
from base.helpers import getMenuInfo
from base.permissions import memberCheck, isCreator, isCoplanner
from forms import EventForm, HikeForm, GenericTripForm, GenericGatheringForm, DinnerForm


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
		context = {'menu' : getMenuInfo(request), 'title' : 'Edit Event', \
			'editeventform' : editeventform, 'event' : event, 'creator' : creator, 'coplanner' : coplanner}

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
					editeventform.save()
					subform.save()

			context['subform'] = subform

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
		
		return HttpResponseRedirect("")	




@login_required(login_url = '/loginRequired/')
def deleteEvent(request, eventid):
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
	
	eventChild = EventModel.getEvent(eventid)
	eventChild.delete()
	event.delete()
	# TODO : delete also from invite table everyone in event

	return HttpResponseRedirect(reverse('base:upcoming'))

@login_required(login_url = '/loginRequired/')  # User have to be logged in to see this view - if not: redirects to loginRequired
def submit_new(request):
	if request.method == "POST":
		eventform = EventForm(request.POST)
		if eventform.is_valid():
			eventform.save()
			return HttpResponseRedirect(reverse('base:eventHome'))
	return HttpResponseRedirect(reverse('base:new_event'))
