from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.core.urlresolvers import reverse

def index(request):
	# TODO
	return render(request, 'index.html')

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
	logout(request)

	return render(request, 'index.html')

def event_home(request, eventid):
	return HttpResponse("Event Home Page")

def login(request):
	return render(request, 'login.html')

def authView(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	
	user = authenticate(username=username, password=password)

	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse('base:home'))

	else:
		return HttpResponseRedirect(reverse('base:invalidLogin'))

def invalidLogin(request):
	return render(request, 'invalidLogin.html')

def register(request):
	return render(request, 'register.html')






