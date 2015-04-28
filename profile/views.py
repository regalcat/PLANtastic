#imported from django and/or python
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout, update_session_auth_hash
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password, is_password_usable
from django.views.generic.edit import FormView
from django.contrib.auth.models import User


#imported from our project
from events.models import EventModel
from base.helpers import getMenuInfo
from forms import ProfileForm, UserForm
from notifications.models import NotificationModel
from invite.models import MembershipModel



@login_required(login_url = '/loginRequired/')  # User have to be logged in to see this view - if not: redirects to login_url
def profile(request):
	user1 = request.user
	profile = user1.profile
	
	context = {'menu' : getMenuInfo(request), 'title' : "Profile", 'membership' : request.user.date_joined, 'name' : request.user.get_short_name(), 'fullname' : request.user.get_full_name(), 'email' : request.user.email, 'username' : request.user.username, 'birthday' : request.user.profile.getBirthday(), 'gender' : request.user.profile.gender, 'description' : request.user.profile.description, 'avatar' : request.user.profile.avatar }
	
	return render(request, 'profile/profile.html', context)

@login_required(login_url = '/loginRequired/')
def otherProfile(request):
	if request.method == "POST":
		otherusername = request.POST['username']
		eventid = request.POST['eventid']

		event = EventModel.objects.filter(eventid = eventid)
		
		otheruser = User.objects.filter(username = otherusername)
		otheruser = otheruser[0]

		events1 = MembershipModel.objects.filter(user = request.user)
		events2 = MembershipModel.objects.filter(user = otheruser)

		boolean = False
		
		for event1 in events1:
			for event2 in events2:
				if event1.event == event2.event:
					boolean = True
					break

		if boolean == False:
			# permission denied
			context = {'menu' : getMenuInfo(request), 'title' : "Permission denied"}
			return render(request, 'profile/notFriends.html', context)

		else:
			context = {'menu' : getMenuInfo(request), 'title' : "View profile", \
			'membership' : otheruser.date_joined, 'fullname' : otheruser.get_full_name(),  \
			'avatar' : otheruser.profile.avatar , 'gender' : otheruser.profile.gender, \
			'description' : otheruser.profile.description, 'event' : event[0]}
			
			return render(request, 'profile/otherProfile.html', context)
		

	else:
		context = {'menu' : getMenuInfo(request), 'title' : "Permission denied"}
		return render(request, 'profile/notFriends.html', context)



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

					return HttpResponseRedirect(reverse('profile:manageAccount'))
	
	return HttpResponseRedirect(reverse('profile:manageAccount'))

@login_required(login_url = '/loginRequired/')  # User have to be logged in to see this view - if not: redirects to login_url
def editInformation(request):
	if request.method == "POST":
		profileform = ProfileForm(request.POST, request.FILES, instance = request.user.profile)
		userform = UserForm(request.POST, instance = request.user)
		if userform.is_valid() and profileform.is_valid():
			avatar = profileform.cleaned_data['avatar']
			profileform.save()
			userform.save()
			profile = request.user.profile
			if avatar:
				profile.avatar = avatar
			profile.save()
			return HttpResponseRedirect(reverse('profile:manageAccount'))


	return HttpResponseRedirect(reverse('profile:manageAccount'))

@login_required(login_url = '/loginRequired/')  # User have to be logged in to see this view - if not: redirects to login_url
def deleteAccount(request):
	return render(request, "profile/deleteAccount.html", {'menu' : getMenuInfo(request), 'title' : "Delete Account Confirmation"})

@login_required(login_url = '/loginRequired/')  # User have to be logged in to see this view - if not: redirects to login_url
def executeDelete(request):

	events = MembershipModel.objects.filter(user = request.user)

	for em in events:
		if em.status == "CR":
			allmembers = MembershipModel.objects.filter(event = em.event)
			for mem in allmembers:
				note = NotificationModel()
				text = "The event " + str(em.event.name) + " that you were a member of has been deleted."
				note.createNewNotification(user = mem.user, text = text)

	request.user.delete()

	return HttpResponseRedirect(reverse('base:index'))

			
