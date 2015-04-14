from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from invite.models import MembershipModel
from models import EventModel
from base.helpers import getMenuInfo, isPreviousEvent, isUpcomingEvent
from tools.ToolManager import ToolManager
from base.permissions import memberCheck, isCreator, isCoplanner

class eventHomeView(View):
	@method_decorator(login_required(login_url = '/loginRequired/'))

	def get(self, request, eventid):
		event = EventModel.getEvent(eventid)
		if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : 'Not Member'})

		
		members = MembershipModel.objects.filter(event = event)
		tools_data = ToolManager.getTools(event)
		context = tools_data['context']
		context.update({'menu' : getMenuInfo(request), 'event' : event, \
			'tools' : tools_data['tools'], 'members' : members})

		#print context['upload_pics']['pics']
		if isPreviousEvent(event):
			permissionevent = EventModel.objects.filter(eventid=eventid)
			if isCreator(request.user, permissionevent[0]):
				context['creator'] =  True
			if isCoplanner(request.user, permissionevent[0]):
				context['coplanner'] = True

		if not isUpcomingEvent(event):

			return render(request, 'events/past_event_home.html', context)
		return render(request, 'events/event_home.html', context)

	@method_decorator(login_required(login_url = '/loginRequired/'))
	def post(self, request, eventid):
		return self.get(request, eventid)
