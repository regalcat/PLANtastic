#Imports from django and/or python
from django.http import HttpResponse
from django.template import RequestContext, loader
from django import forms
from django.views.generic.edit import FormView

#Imports from our project
from base.forms import InviteForm
from base.events.models import EventModel
from base.Helpers import getMenuInfo


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
		event = getEvent(eventid)
		InviteForm.send_email(to, event)
		#TODO Make this go to a template that confirms that it worked
		return HttpResponse("Thank you for inviting people!")
