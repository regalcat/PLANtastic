from django.shortcuts import render
from django.views.generic import View

from django.http import HttpResponse

from base.events.models import EventModel
from base.Helpers import getMenuInfo
from tools.ToolManager import ToolManager

class EventHomeView(View):
  def get(self, request, eventid):
    event = EventModel.getEvent(eventid)
    tools = ToolManager.getTools(event)
    return render(request, 'events/event_home.html', {'menu' : getMenuInfo(request), 'event': event, 'tools' : tools})

  def post(self, request, eventid):
    return HttpResponse("Post Request")
