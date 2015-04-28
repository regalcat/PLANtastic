from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import MsPaymentModel

from events.models import EventModel
from invite.models import MembershipModel

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
		event=EventModel.objects.filter(eventid=eventid)
		members = MembershipModel.objects.filter(event=eventid)
		context = {'eventid':eventid, 'members':members,}
		#return super(RecordPaymentView, self).get(self, request)
		return render(request, 'money_share/record_payment_form.html', context)

	@method_decorator(login_required(login_url = '/loginRequired/'))
	def post(self, request, eventid):

		event = EventModel.getEvent(eventid)
		if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})

		payer=User.objects.get(username=request.POST['payer'])
		receiver=User.objects.get(username=request.POST['receiver'])
		payment = MsPaymentModel(event=event, payer=payer, receiver=receiver,\
			amount=request.POST['amount'])
		payment.save()
		context = {'eventid':eventid}
		self.eventid=eventid
		#return super(RecordPaymentView, self).post(self, request)
		return HttpResponseRedirect(reverse('events:tools:money_share:money_share.index',  kwargs={'eventid':eventid,}))

	def form_valid(self, form):
		self.success_url = "../"
		form.instance.event_id=self.eventid
		return super(RecordPaymentView, self).form_valid(form)

