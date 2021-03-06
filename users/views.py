from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.templatetags.static import static
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout, update_session_auth_hash
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password, is_password_usable
from django.views.generic.edit import FormView
from friends.models import FriendList
from django.contrib.auth.models import User

from os import listdir
from os.path import isfile, join

#imported from our project
from events.models import EventModel, HikeEventModel, DinnerEventModel, GenericTripModel,\
	GenericGatheringModel
from invite.models import InviteModel, MembershipModel
from forms import UserRegistrationForm
from base.helpers import getMenuInfo

def logout(request):
	authLogout(request)
	return HttpResponseRedirect(reverse('base:index'))

def login(request):
	return render(request, 'users/login.html')

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
	return render(request, 'users/invalidLogin.html')

def loginRequired(request):
	return render(request, 'users/loginRequired.html')

def registerSuccess(request):
	return render(request, 'users/registerSuccess.html')


def register(request):
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			user = User.objects.get(username=request.POST['username'])
			friendlist=FriendList(user=user)
			friendlist.save()
			return HttpResponseRedirect(reverse('base:registerSuccess'))

	args = {}
	args['form'] = UserRegistrationForm()
	return render(request, 'users/register.html', args)	
