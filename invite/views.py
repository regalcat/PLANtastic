#Imports from django and python
import string
import random
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django import forms
from django.views.generic.edit import FormView
from os import listdir
from os.path import isfile, join
from django.templatetags.static import static
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password, is_password_usable
from django.views.generic.edit import FormView


#Imports from our project
from forms import InviteForm
from base.Helpers import getMenuInfo
from events.models import EventModel, 
from invite.models import MembershipModel, InviteModel


def test(request):
	template = loader.get_template('index.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

#The class that handles inviting people via email and then displays an html page
class InviteView(FormView):
	temp_name = ''
	form_class = InviteForm
	success_url = r'^(?P<eventid>\d+)/$'
	
	def valid_email(self, form):
		
		form.send_invite()
		return super(InviteView, self).valid_email(form)

	def get(self, request, eventid):
		user = request.user
		cur_event = EventModel.getEvent(eventid)
		template = loader.get_template("invite.html")
		context = RequestContext(request, {'event' : cur_event, 'user' : user, 'cur_path' : request.get_full_path(), 'title' : "Invite friends", 'menu' : getMenuInfo(request)})
		return HttpResponse(template.render(context))

	def post(self, request, eventid):
		to = request.POST['email']
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
		
		template = loader.get_template("inviteSuccess.html")
		context = RequestContext(request, {'event' : event, 'user' : request.user, 'cur_path' : request.get_full_path(), 'title' : "Invite Success", 'menu' : getMenuInfo(request)})
		return HttpResponse(template.render(context))

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


