from django import forms
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from tools.ride_share.models import Car, Person, Riders
from events.models import EventModel

class AddCarView(CreateView):
	template_name='ride_share/add_car_form.html'
	model = Car
	fields = ['seats',]
	exclude = ['driver',]
	


	def get(self, request, eventid):
		self.eventid=eventid
		#self.driver = request.user
		return super(AddCarView, self).get(self, request)

	def post(self, request, eventid):
		self.eventid=eventid
		#self.driver = request.user
		event = EventModel.getEvent(eventid)
		person = Person()
		person = person.newPerson(event=event, personid=request.user, status='DR')
		person.save()
		driver1 = Person.objects.filter(event=event, personid = request.user)
		self.driver = driver1[0].personid.id
		self.seats = request.POST['seats']
		#car=Car()
		#car = car.newCar(event=event, seats=request.POST['seats'], driver=driver1[0] )

		#if (car.open_seats == None):
		#	car.open_seats = request.POST['seats']		
		#car.save()
		#car.passengers.add(person)
		#car.save()
		return super(AddCarView, self).post(self, request)

	def form_valid(self, form):
		self.success_url = "http://"+self.request.get_host()+"/"+self.eventid+"/tools/ride_share"
		form.instance.event_id=self.eventid
		form.instance.driver_id=self.driver
		return super(AddCarView, self).form_valid(form)
