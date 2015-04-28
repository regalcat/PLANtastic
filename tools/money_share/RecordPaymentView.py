from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import MsPaymentModel
from events.models import EventModel
from invite.models import MembershipModel

class RecordPaymentView(CreateView):
	template_name='money_share/record_payment_form.html'
	model = MsPaymentModel
	fields = ['payer', 'receiver', 'amount']

	def get(self, request, eventid):
		self.eventid=eventid
		event=EventModel.objects.filter(eventid=eventid)
		members = MembershipModel.objects.filter(event=eventid)
		context = {'eventid':eventid, 'members':members,}
		#return super(RecordPaymentView, self).get(self, request)
		return render(request, 'money_share/record_payment_form.html', context)

	def post(self, request, eventid):
		event=EventModel.objects.get(eventid=eventid)
		payer=User.objects.get(username=request.POST['payer'])
		receiver=User.objects.get(username=request.POST['receiver'])
		payment = MsPaymentModel(event=event, payer=payer, receiver=receiver,\
			amount=request.POST['amount'])
		payment.save()
		self.eventid=eventid
		return super(RecordPaymentView, self).post(self, request)

	def form_valid(self, form):
		self.success_url = "../"
		form.instance.event_id=self.eventid
		return super(RecordPaymentView, self).form_valid(form)

