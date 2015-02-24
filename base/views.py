from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
	# TODO
	return HttpResponse("Index page")

def home(request):
	# TODO
	return HttpResponse("Home Page")

def upcoming(request):
	# TODO
	return HttpResponse("Upcoming Trips Page")

def past(request):
	# TODO
	return HttpResponse("Past Events Page")

def profile(request):
	# TODO
	return HttpResponse("Profile Page")

def manage_account(request):
	# TODO
	return HttpResponse("Manage Account")

def logout(request):
	# TODO
	return HttpResponse("Logout Page")

def event_home(request, eventid):
	return HttpResponse("Event Home Page")
