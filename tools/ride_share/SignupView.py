from django import forms
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse
from django.template import RequestContext, loader

from base.helpers import getMenuInfo
from tools.ride_share.models import Car, Person, Riders
from events.models import EventModel
from forms import PersonForm

class SignupView(CreateView):
	template_name='ride_share/sign_up_form.html'
	model = Person
	fields = ('address',)

	

	def get(self, request, eventid):
		self.eventid=eventid
		event = EventModel.objects.filter(eventid=eventid)
		#personid = request.user
		cars = Car.cars.filter(event = event)
		person = Person(personid = request.user)
		open_seats=0
		passengers=None
		personform = PersonForm(personid = request.user)
		for car in cars:
			car.open_seats = car.getOpenSeats(eventid)
			passengers = car.getPassengerList(eventid)

		context = {'menu' : getMenuInfo(request), 'title' : "Sign Up", 'cars' : cars, 'event' : event, \
		 'Open_Seats' : open_seats,'personform':personform}	
		return super(SignupView, self).get(self, request, context)
		#return render(request, 'ride_share/main.html', context)

	def post(self, request, eventid):
		self.eventid=eventid
		event = EventModel.objects.filter(eventid=eventid)
		cars = Car.cars.filter(event =event)
		user= request.user
		status='Passenger'
		car = request.POST[car]
		for passenger in car.passengers.all():
			if (passenger.status == 'DR'):
				driver = passenger.personid.username
		person = Person(personid=user, status=status)
		car.passengers.add(person)
		person.save()
		car.save()
		return super(Person, self).post(self, request)

	def form_valid(self, form):
		self.success_url = "http://"+self.request.get_host()+"/"+self.eventid+"/tools/ride_share"
		form.instance.event_id=self.eventid
		return super(Person, self).form_valid(form)
