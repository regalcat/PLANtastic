from django.http import HttpResponse
from django.template import RequestContext, loader

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from base.helpers import getMenuInfo
from events.models import EventModel
from tools.ride_share.models import RideModel, RideSignupModel
from tools.ToolView import ToolView


class RideShareView(ToolView):
	tile_template = "ride_share/ride_share_tile.html"

	@staticmethod
	def getIdentifier():
		return "ride_share"

	def get(self, request, eventid):
		user = request.user
		cur_event = EventModel.getEvent(eventid)
		cars = RideModel.cars.filter(event=cur_event)
		for car in cars:
			
			car.signups = RideSignupModel.objects.filter(rideid = car).exclude(user=request.user)
			car.available = car.seats
			car.your_signup = RideSignupModel.objects.filter(rideid=car, user=request.user)
			car.signedup = 0
			for signup in car.signups:
				car.signedup +=1 
				car.available -= 1
			if car.your_signup.count() == 0 or car.available<=0:
				car.your_signup = False
			else:
				car.your_signup = car.your_signup[0]
				car.available -= 1
		admin = False
#		if (user.isDriver()):
		if (True):
			admin = True
		template = loader.get_template("ride_share/main.html")
		context = RequestContext(request, {'Vehicles' : cars, 'event' : cur_event, 'cur_path' : request.get_full_path(), 'title' : "Ride Share", 'menu': getMenuInfo(request) })
		return HttpResponse(template.render(context))

	@csrf_exempt
	def post(self, request, eventid):
		ajax = request.POST.get('ajax', False)
		cur_event=EventModel.getEvent(eventid)
		car = RideModel.car.get(id=request.POST['rideid'], event=cur_event)
		signup = RideSignupModel.objects.update_or_create(rideid=ride, user = request.user, event=cur_event, defaults={'seats' : request.POST['seats']})
		if ajax:
			# TODO - return sum of all people in car
			cars = RideSignupModel.objects.filter(rideid=ride, event=cur_event)
			total = 0
			for car in cars:
				total += car.seats
			return HttpResponse(total)
		return self.get(request, eventid)
