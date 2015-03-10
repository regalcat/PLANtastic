from Helpers import getMenuInfo
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from base.events.models import EventModel


def index(request):
	return render(request, 'index.html')

def home(request):
	# TODO
	return render(request, 'home.html', {'menu' : getMenuInfo(request), 'title' : "Home"})

def upcoming(request):
	# TODO
	return HttpResponse("Upcoming Events Page")

def past(request):
	# TODO
	return HttpResponse("Past Events Page")

@login_required(login_url = '/login/')  # User have to be logged in to see this view - if not: redirects to login_url
def profile(request):	
	return render(request, 'profile.html', {'menu' : getMenuInfo(request),'title' : "Profile", 'membership' : request.user.date_joined})

def manageAccount(request):
	return render(request, 'manageAccount.html')

def logout(request):
	authLogout(request)
	return HttpResponseRedirect(reverse('base:index'))

def event_home(request, eventid):
	# TODO - replace Event Home with the event title
	return render(request, 'event_home.html', {'menu' : getMenuInfo(request), 'title' : "Event Home"})

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

def registerSuccess(request):
	return render(request, 'registerSuccess.html')

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('base:registerSuccess'))

	args = {}
	args['form'] = UserCreationForm()
	return render(request, 'register.html', args)

def checkInformation(request):
	if request.method == "POST":
		oldpassword = request.POST.get("oldpassword")
		newpassword = request.POST.get("newpassword1")

		if oldpassword == request.user.password:
		
	return render(request, 'manageAccount.html')
			
		

def new(request):
	if request.method == "POST":
		form = EventModel.createEvent(EventModel,request.POST['eventName'])
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('http://'+request.get_host()+"/"+event.eventId)
		
	template = loader.get_template('events/new.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))











