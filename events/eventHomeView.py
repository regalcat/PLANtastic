from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


from invite.models import MembershipModel
from models import EventModel
from base.helpers import getMenuInfo, isPreviousEvent
from tools.ToolManager import ToolManager
from base.permissions import memberCheck



class eventHomeView(View):
	@method_decorator(login_required(login_url = '/loginRequired/'))

	def get(self, request, eventid):
		event = EventModel.getEvent(eventid)
		if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html')
	
		tools = ToolManager.getTools(event)
		members = MembershipModel.objects.filter(event = event)
		if isPreviousEvent(event):
			return render(request, 'events/past_event_home.html', {'menu' : getMenuInfo(request), \
				'event' : event, 'tools' : tools, 'members' : members})
		return render(request, 'events/event_home.html', \
			{'menu' : getMenuInfo(request), 'event': event, 'tools' : tools, 'members' : members})

	@method_decorator(login_required(login_url = '/loginRequired/'))
	def post(self, request, eventid):
		return self.get(request, eventid)
