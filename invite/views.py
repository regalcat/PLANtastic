import string
import random

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from base.helpers import getMenuInfo
from base.permissions import getMemberObject, memberCheck
from events.models import EventModel 
from .forms import InviteForm
from .models import MembershipModel, InviteModel
from notifications.models import NotificationModel

#The class that handles inviting people via email and then displays an html page
class InviteView(FormView):
	temp_name = ''
	form_class = InviteForm
	success_url = r'^(?P<eventid>\d+)/$'
	
	@method_decorator(login_required(login_url = '/loginRequired/'))
	def valid_email(self, form):
		
		form.send_invite()
		return super(InviteView, self).valid_email(form)

	@method_decorator(login_required(login_url = '/loginRequired/'))
	def get(self, request, eventid):
		event = EventModel.getEvent(eventid)
		if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})

		user = request.user
		cur_event = EventModel.getEvent(eventid)
		template = loader.get_template("invite/invite.html")
		context = RequestContext(request, {'event' : cur_event, 'user' : user, 'cur_path' : request.get_full_path(), 'title' : "Invite friends", 'menu' : getMenuInfo(request)})
		return HttpResponse(template.render(context))

	@method_decorator(login_required(login_url = '/loginRequired/'))
	def post(self, request, eventid):
		event = EventModel.getEvent(eventid)
		if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})

			#if request.POST['email']!=""
		to = request.POST['email']
		#if request.POST['username']!=""
		#	to = User.objects.filter(username = username).email
		
		event = EventModel.getEvent(eventid)
		rstring = ""
		for i in range(0,16):
			rstring+=random.choice(string.ascii_letters + string.digits)
		
		#instance of InviteModel
		invite=InviteModel(inviteEmail=to, inviteEvent=event, inviteString=rstring)
		#Sends the email
		InviteForm.send_email(to, event, rstring)
		#Saves the invite to the table
		invite.save()
		#Not happy with this going to the template, but I'll deal for now

		notifications = NotificationModel()
		text = "You have just invited " + str(to) + " to the event " + str(event.name) +"."
		link = "events:eventHome"
		eventarg = int(invite.inviteEvent.eventid)
		btntext = "Go to event"
		notifications = notifications.createButtonNotification(user=request.user, text = text, \
				link=link, btnText=btntext, eventarg = eventarg, friendarg= None)

		
		template = loader.get_template("invite/inviteSuccess.html")
		context = RequestContext(request, {'event' : event, 'user' : request.user, 'cur_path' : request.get_full_path(), 'title' : "Invite Success", 'menu' : getMenuInfo(request)})
		return HttpResponse(template.render(context))

@login_required(login_url = '/loginRequired/')
def usernameInvite(request, eventid):
	if request.method == "POST":
		username = request.POST["username"]
		event = EventModel.getEvent(eventid)
		user = User.objects.filter(username = username)
		if user.count() != 1:
			return HttpResponseRedirect(reverse("events:invite", kwargs={'eventid':eventid}))
		if memberCheck(user[0], event) == True:
			return HttpResponseRedirect(reverse("events:invite", kwargs={'eventid':eventid}))

		rstring = ""
		for i in range(0,16):
			rstring+=random.choice(string.ascii_letters + string.digits)

		invite=InviteModel(inviteEmail= user[0].email, inviteEvent=event, inviteString=rstring)
		invite.save()

		notifications = NotificationModel()
		text = "You just got invited to the event " + str(event.name) + \
		". Join the event by using this confirmationstring: " \
		+ rstring + " on the join event page."
		notifications = notifications.createNewNotification(user=user[0], text = text)
				

		notifications = NotificationModel()
		text = "You have just invited " + str(username) + " to the event " + str(event.name) +"."
		link = "events:eventHome"
		eventarg = int(invite.inviteEvent.eventid)
		btntext = "Go to event"
		notifications = notifications.createButtonNotification(user=request.user, text = text, \
				link=link, btnText=btntext, eventarg = eventarg, friendarg= None)

		context = {'event' : event, 'user' : request.user, 'cur_path' : request.get_full_path(), 'title' : "Invite Success", 'menu' : getMenuInfo(request)}
		return render(request, "invite/inviteSuccess.html", context)



@login_required(login_url = '/loginRequired/')  # User have to be logged in to see this view - if not: redirects to loginRequired
def join_event(request):
	if (request.method == "POST"):
		# TODO - add error checking
		string = request.POST['string']
		invite = InviteModel.objects.filter(inviteString = string)
		#print invite.count()
		#print invite[0].inviteEmail
		#print request.user.email
		
		if (invite.count() != 1 or invite[0].inviteEmail != request.user.email):
			return render(request, 'invite/join.html', { 'menu' : getMenuInfo(request), \
				'title' : "Join Event" , 'error': True, 'error_message' : "Invalid Confirmation String" })
		else:
			invite = invite[0]
		if (MembershipModel.objects.filter(event=invite.inviteEvent, user=request.user).count() == 0):
			member = MembershipModel(event=invite.inviteEvent, user=request.user, status=MembershipModel.MEMBER)
			member.save()
						
			creator = MembershipModel.objects.filter(event=invite.inviteEvent, status = "CR")
			notifications = NotificationModel()
			text = str(request.user.username) + " has just joined your event " + str(invite.inviteEvent.name) + "."
			link = "events:eventHome"
			eventarg = int(invite.inviteEvent.eventid)
			btntext = "Go to event"
	

			notifications = notifications.createButtonNotification(user=creator[0].user, \
					 text = text, link=link, btnText=btntext, eventarg = eventarg, friendarg= None)
			invite.delete()
	
		return HttpResponseRedirect('http://'+str(request.get_host())+'/'+str(invite.inviteEvent.eventid))
	return render(request, 'invite/join.html', { 'menu' : getMenuInfo(request), 'title' : "Join Event" })

## REUSABLE STRING FOR THE DEMO!
@login_required(login_url = '/loginRequired/')
def tempJoin(request):
	if (request.method == "POST"):
		string = request.POST['string']
		invite = InviteModel.objects.filter(inviteString = string)
	
		if (invite.count() != 1):
			return render(request, 'invite/join.html', { 'menu' : getMenuInfo(request), \
			'title' : "Join Event" , 'error': True, 'error_message' : "Invalid Confirmation String" })
		else:
			invite = invite[0]
	
		if (MembershipModel.objects.filter(event=invite.inviteEvent, user=request.user).count() == 0):
				member = MembershipModel(event=invite.inviteEvent, user=request.user, status=MembershipModel.MEMBER)
				member.save()
						
				creator = MembershipModel.objects.filter(event=invite.inviteEvent, status = "CR")
				notifications = NotificationModel()
				text = str(request.user.username) + " has just joined your event " + str(invite.inviteEvent.name) + "."
				link = "events:eventHome"
				eventarg = int(invite.inviteEvent.eventid)
				btntext = "Go to event"
	

				notifications = notifications.createButtonNotification(user=creator[0].user, \
					 text = text, link=link, btnText=btntext, eventarg = eventarg, friendarg= None)
		return HttpResponseRedirect('http://'+str(request.get_host())+'/'+str(invite.inviteEvent.eventid))
	return render(request, 'invite/join.html', { 'menu' : getMenuInfo(request), 'title' : "Join Event" })


