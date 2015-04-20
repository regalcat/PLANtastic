from django import forms
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from tools.ride_share.models import RideModel, RideSignupModel
from events.models import EventModel

class AddCarView(CreateView):
	template_name='ride_share/add_car_form.html'
	model = RideModel
	fields = ['seats', 'driver']
	


	def get(self, request, eventid):
		self.eventid=eventid
		return super(AddCarView, self).get(self, request)

	def post(self, request, eventid):
		self.eventid=eventid
		event = EventModel.getEvent(eventid)
		ride = RideSignupModel(event=event, user=request.user, status='DR')
		
		return super(AddCarView, self).post(self, request)

	def form_valid(self, form):
		self.success_url = "http://"+self.request.get_host()+"/"+self.eventid+"/tools/ride_share"
		form.instance.event_id=self.eventid
		return super(AddCarView, self).form_valid(form)
