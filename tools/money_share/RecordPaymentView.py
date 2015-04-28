from django import forms
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import MsPaymentModel
from base.permissions import memberCheck
from events.models import EventModel

class RecordPaymentView(CreateView):
	template_name='money_share/record_payment_form.html'
	model = MsPaymentModel
	fields = ['payer', 'receiver', 'amount']

	@method_decorator(login_required(login_url = '/loginRequired/'))
	def get(self, request, eventid):
		event = EventModel.getEvent(eventid)
		if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})

		self.eventid=eventid
		return super(RecordPaymentView, self).get(self, request)

	@method_decorator(login_required(login_url = '/loginRequired/'))
	def post(self, request, eventid):
		event = EventModel.getEvent(eventid)
		if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})

		self.eventid=eventid
		return super(RecordPaymentView, self).post(self, request)

	def form_valid(self, form):
		self.success_url = "../"
		form.instance.event_id=self.eventid
		return super(RecordPaymentView, self).form_valid(form)

