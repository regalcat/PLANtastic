from django.shortcuts import render
from django.views.generic import View

from django.http import HttpResponse

from models import EventModel
from base.helpers import getMenuInfo, isPreviousEvent
from tools.ToolManager import ToolManager

class EventHomeView(View):
	def get(self, request, eventid):
		event = EventModel.getEvent(eventid)
		tools = ToolManager.getTools(event)
		if isPreviousEvent(event):
			return render(request, 'events/past_event_home.html', {'menu' : getMenuInfo(request), \
				'event' : event, 'tools' : tools})
		return render(request, 'events/event_home.html', \
			{'menu' : getMenuInfo(request), 'event': event, 'tools' : tools})

	def post(self, request, eventid):
		return self.get(request, eventid)
