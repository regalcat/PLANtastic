from django import forms
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from tools.ride_share.models import RideModel, RideSignupModel

class SignupView(CreateView):
	template_name='ride_share/sign_up_form.html'
	model = RideSignupModel
	fields = ['address']
	
	

	def get(self, request, eventid):
		self.eventid=eventid
		return super(SignupView, self).get(self, request)

	def post(self, request, eventid):
		self.eventid=eventid
		user= request.user
		status='Passenger'
		return super(SignupView, self).post(self, request)

	def form_valid(self, form):
		self.success_url = "http://"+self.request.get_host()+"/"+self.eventid+"/tools/ride_share"
		form.instance.event_id=self.eventid
		return super(SignupView, self).form_valid(form)
