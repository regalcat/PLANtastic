from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, 'index.html')

def home(request):
	return render(request, 'home.html', {'username' : request.user.username})

def upcoming(request):
	# TODO
	return HttpResponse("Upcoming Trips Page")

def past(request):
	# TODO
	return HttpResponse("Past Events Page")

@login_required(login_url = '/login/')  # User have to be logged in to see this view - if not: redirects to login_url
def profile(request):	
	return render(request, 'profile.html', {'username' : request.user.username, 'membership' : request.user.date_joined})

def manage_account(request):
	return render(request, 'manageAccount.html')

def logout(request):
	authLogout(request)
	return HttpResponseRedirect(reverse('base:index'))

def event_home(request, eventid):
	return HttpResponse("Event Home Page")

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










