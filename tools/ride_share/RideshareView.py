from django.http import HttpResponse
from django.template import RequestContext, loader

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from base.helpers import getMenuInfo
from events.models import EventModel
from tools.ride_share.models import Car, Person, Riders
from tools.ToolView import ToolView

class RideshareView(ToolView):
	tile_template = "ride_share/ride_share_tile.html"

	@staticmethod
	def getIdentifier():
		return "ride_share"
	

	@staticmethod
	def getContext(event):
		eventid = event.eventid
		
		cars=Car.cars.filter(event=event)
		for car in cars:
			car.open_seats = car.getOpenSeats(eventid)
		ccount = cars.count()
		context = {'cars':cars, 'ccount':ccount}

		return context
