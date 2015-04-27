from django.http import HttpResponse
from django.template import RequestContext, loader

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from base.helpers import getMenuInfo
from events.models import EventModel
from tools.maps.models import Gmap
from tools.ToolView import ToolView

class MapView(ToolView):
	tile_template = "maps/maps.html"

	@staticmethod
	def getIdentifier():
		return "maps"
	

	@staticmethod
	def getContext(event):
		eventid = event.eventid
		
		gmaps=Gmap.objects.filter(event=event)
		for gmap in gmaps:
			gmap.location = gmap.location
		
		context = {'event' : event, 'gmaps':gmaps }

		return context






