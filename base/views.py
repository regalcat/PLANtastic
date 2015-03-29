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

from os import listdir
from os.path import isfile, join

#imported from our project
from base.events.models import EventModel, HikeEventModel, DinnerEventModel, GenericTripModel, GenericGatheringModel, InviteModel
from base.invite.models import MembershipModel
from forms import UserRegistrationForm
from Helpers import getMenuInfo

def index(request):
	return render(request, 'index.html')

def home(request):
	# TODO
	return render(request, 'home.html', {'menu' : getMenuInfo(request), 'title' : "Home"})

def upcoming(request):
	return render(request, 'upcoming.html', {'menu' : getMenuInfo(request), 'title' : "Upcoming Events"})

@login_required(login_url = '/loginRequired/')
def past(request):
	
	return render(request, 'past.html', { 'menu' : getMenuInfo(request), 'title' : "Past Events"})

def logout(request):
	authLogout(request)
	return HttpResponseRedirect(reverse('base:index'))

def login(request):
	return render(request, 'login.html')

def authView(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	
	user = authenticate(username=username, password=password)

	if user is not None:
		authLogin(request, user)
		return HttpResponseRedirect(reverse('base:home'))

	else:
		return HttpResponseRedirect(reverse('base:invalidLogin'))

def invalidLogin(request):
	return render(request, 'invalidLogin.html')

def loginRequired(request):
	return render(request, 'loginRequired.html')

def registerSuccess(request):
	return render(request, 'registerSuccess.html')

def register(request):
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('base:registerSuccess'))

	args = {}
	args['form'] = UserRegistrationForm()
	return render(request, 'register.html', args)			
		
@login_required(login_url = '/loginRequired/')  # User have to be logged in to see this view - if not: redirects to loginRequired
def new(request):
	if request.method == "POST":
		event = EventModel()
		event.createEvent(eventName=request.POST['eventName'],eventLocation=request.POST['eventLocation'], \
			eventDateStart=request.POST['eventDateStart'],eventType=request.POST['eventType'],eventDescription=request.POST['eventDescription'])
		event.save()

		member = MembershipModel(event=event, user=request.user, status=MembershipModel.CREATOR)
		member.save()

		if (request.POST['eventType'] == u'hike'):
			eventDuration=request.POST['eventDuration']
			eventDistance=request.POST['eventDistance']
			eventElevation=request.POST['eventElevation']
			eventDateEnd=request.POST['eventDateEnd']

			if eventDistance == '':
				eventDistance = None
			if eventElevation == '':
				eventElevation = None
			if eventDateEnd == '':
				eventDateEnd = None
			
			event = HikeEventModel(event.eventid, \
				eventName=request.POST['eventName'], eventLocation=request.POST['eventLocation'], \
				eventDateStart=request.POST['eventDateStart'],eventDescription=request.POST['eventDescription'], \
				eventDateEnd=eventDateEnd, eventDuration=eventDuration, eventDistance=eventDistance, 					eventElevation=eventElevation, eventDifficulty=request.POST['difficulty'])
			event.save()

		if (request.POST['eventType'] == u'otherTrip'):
			eventDateEnd=request.POST['eventDateEnd']
			if eventDateEnd == '':
				eventDateEnd = None

			event = GenericTripModel(event.eventid, \
				eventName=request.POST['eventName'], eventLocation=request.POST['eventLocation'], \
				eventDateStart=request.POST['eventDateStart'],eventDescription=request.POST['eventDescription'], 					eventDateEnd=eventDateEnd)
			event.save()

		if (request.POST['eventType'] == u'otherGathering'):
			eventDateEnd=request.POST['eventDateEnd']
			if eventDateEnd == '':
				eventDateEnd = None

			event = GenericGatheringModel(event.eventid, \
				eventName=request.POST['eventName'], eventLocation=request.POST['eventLocation'], \
				eventDateStart=request.POST['eventDateStart'],eventDescription=request.POST['eventDescription'], 					eventDateEnd=eventDateEnd)
			event.save()

		if (request.POST['eventType'] == u'dinner'):
			eventDateEnd=request.POST['eventDateEnd']
			if eventDateEnd == '':
				eventDateEnd = None

			event = DinnerEventModel(event.eventid, \
				eventName=request.POST['eventName'], eventLocation=request.POST['eventLocation'], \
				eventDateStart=request.POST['eventDateStart'],eventDescription=request.POST['eventDescription'], 					eventDateEnd=eventDateEnd)
			event.save()

		return HttpResponseRedirect('http://'+str(request.get_host())+'/'+str(event.eventid))
		
	return render(request, 'events/new.html', { 'menu' : getMenuInfo(request), 'title' : "Create Events"})

def coverPic(request):
	files = '{"pics": ['
	path = 'base/static/cover_pics/'
	temp = listdir(path);
	for f in temp:
		if isfile(join(path, f)):
			filename = static('cover_pics/' + f)
			files += '"'+filename+'",'
	files = files[:-1]
	files += "]}"
	return HttpResponse(files)

@login_required(login_url = '/loginRequired/')  # User have to be logged in to see this view - if not: redirects to loginRequired
def join_event(request):
	if (request.method == "POST"):
		# TODO - add error checking
		string = request.POST['string']
		invite = InviteModel.objects.filter(inviteString = string)
		print invite.count()
		print invite[0].inviteEmail
		print request.user.email
		if (invite.count() != 1 or invite[0].inviteEmail != request.user.email):
			return render(request, 'invite/join.html', { 'menu' : getMenuInfo(request), \
				'title' : "Join Event" , 'error': True, 'error_message' : "Invalid Confirmation String" })
		invite = invite[0]
		if (MembershipModel.objects.filter(event=invite.inviteEvent, user=request.user).count() == 0):
			member = MembershipModel(event=invite.inviteEvent, user=request.user, status=MembershipModel.COPLANNER)
			member.save()
		return HttpResponseRedirect('http://'+str(request.get_host())+'/'+str(invite.inviteEvent.eventid))
	return render(request, 'invite/join.html', { 'menu' : getMenuInfo(request), 'title' : "Join Event" })
