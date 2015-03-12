#imported from django and/or python
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout, update_session_auth_hash
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password, is_password_usable
from django.views.generic.edit import FormView

#imported from our project
from base.events.models import EventModel
from forms import InviteForm
from forms import UserRegistrationForm
from Helpers import getMenuInfo

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
	context = {'menu' : getMenuInfo(request),'title' : "Profile", 'membership' : request.user.date_joined, 'name' : request.user.get_short_name(), 'fullname' : request.user.get_full_name(), 'email' : request.user.email, 'username' : request.user.username}
	
	return render(request, 'profile.html', context)

@login_required(login_url = '/login/')  # User have to be logged in to see this view - if not: redirects to login_url
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
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('base:registerSuccess'))

	args = {}
	args['form'] = UserRegistrationForm()
	return render(request, 'register.html', args)

@login_required(login_url = '/login/')  # User have to be logged in to see this view - if not: redirects to login_url
def checkInformation(request):
	if request.method == "POST":
		oldpassword = request.POST.get("oldpassword")
		newpassword = request.POST.get("newpassword1")
		newpassword2 = request.POST.get("newpassword2")

		if newpassword == newpassword2:
			if request.user.check_password(oldpassword):
				encodedpassword = make_password(newpassword)

				if is_password_usable(encodedpassword):
					request.user.set_password(newpassword)
					request.user.save()
					update_session_auth_hash(request, request.user)

					return HttpResponseRedirect(reverse('base:profile'))
		
	return render(request, 'manageAccount.html')
			
		
@login_required(login_url = '/login/')  # User have to be logged in to see this view - if not: redirects to login_url
def new(request):
	if request.method == "POST":
		event = EventModel.createEvent(request.POST['eventName'],request.POST['eventLocation'],request.POST['eventDateStart'],request.POST['eventType'],request.POST['eventDescription'])
		event.save()
		return HttpResponseRedirect('http://'+str(request.get_host())+'/'+str(event.eventid))
		
	template = loader.get_template('events/new.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

# This method returns the email invite form
class InviteView(FormView):
        template_name = 'invite.html'
        form_class = InviteForm
        success_url = '/invite-sent/'

        #Called when a valid form is submitted
        def form_valid(self, form):
                form.send_email()
                return super(InviteView, self).form_valid(form)










