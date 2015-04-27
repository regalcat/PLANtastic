from django import forms
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import MsPaymentModel

class RecordPaymentView(CreateView):
	template_name='money_share/record_payment_form.html'
	model = MsPaymentModel
	fields = ['payer', 'receiver', 'amount']

	def get(self, request, eventid):
		self.eventid=eventid
		return super(RecordPaymentView, self).get(self, request)

	def post(self, request, eventid):
		self.eventid=eventid
		return super(RecordPaymentView, self).post(self, request)

	def form_valid(self, form):
		self.success_url = "../"
		form.instance.event_id=self.eventid
		return super(RecordPaymentView, self).form_valid(form)

