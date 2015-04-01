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
from events.models import EventModel
from base.helpers import getMenuInfo
from forms import ProfileForm, UserForm




@login_required(login_url = '/loginRequired/')  # User have to be logged in to see this view - if not: redirects to login_url
def profile(request):
	user1 = request.user
	profile = user1.profile
	
	context = {'menu' : getMenuInfo(request), 'title' : "Profile", 'membership' : request.user.date_joined, 'name' : request.user.get_short_name(), 'fullname' : request.user.get_full_name(), 'email' : request.user.email, 'username' : request.user.username, 'birthday' : request.user.profile.getBirthday(), 'gender' : request.user.profile.gender, 'description' : request.user.profile.description}
	
	return render(request, 'profile/profile.html', context)



@login_required(login_url = '/loginRequired/')  # User have to be logged in to see this view - if not: redirects to login_url
def manageAccount(request):
	user = request.user
	profile = user.profile
	profileform = ProfileForm(instance = profile)
	userform = UserForm(instance = user)
	return render(request, 'profile/manageAccount.html', {'profileform' : profileform, 'userform' : userform, 'menu' : getMenuInfo(request), 'title' : "Manage Account"})



@login_required(login_url = '/loginRequired/')  # User have to be logged in to see this view - if not: redirects to login_url
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

					return HttpResponseRedirect(reverse('profile:ManageAccount'))
	
	return HttpResponseRedirect(reverse('profile:manageAccount'))

@login_required(login_url = '/loginRequired/')  # User have to be logged in to see this view - if not: redirects to login_url
def editInformation(request):
	if request.method == "POST":
		profileform = ProfileForm(request.POST, instance = request.user.profile)
		userform = UserForm(request.POST, instance = request.user)
		if userform.is_valid() and profileform.is_valid():
			profileform.save()
			userform.save()
			return HttpResponseRedirect(reverse('profile:manageAccount'))


	return HttpResponseRedirect(reverse('profile:manageAccount'))

			
