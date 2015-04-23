from django.http import HttpResponse
from django.template import RequestContext, loader

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from base.helpers import getMenuInfo
from events.models import EventModel
from tools.ride_share.models import Car, Person, Riders
from tools.ToolView import ToolView


class RideShareView(ToolView):
	tile_template = "ride_share/ride_share_tile.html"

	@staticmethod
	def getIdentifier():
		return "ride_share"

	def getContext(request, eventid):
		user = request.user
		event = EventModel.getEvent(eventid)
		cars = Car.cars.filter(event=event[0])
		for car in cars:
			car.open_seats = car.getOpenSeats(eventid)	
		ccount = cars.count()		
		#template = loader.get_template("ride_share/ride_share_tile.html")
		context = RequestContext(request, {'menu': getMenuInfo(request) ,'title' : "Ride Share",'ccount': ccount,\
		'cars' : cars, 'event' : cur_event, 'cur_path' : request.get_full_path() })
		return HttpResponse(template.render(context))

	@csrf_exempt
	def post(self, request, eventid):
		cur_event=EventModel.getEvent(eventid)
		cars = Car.cars.filter(event=cur_event)
		return self.get(request, eventid)
