from django import forms
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import MsItemModel
from base.permissions import memberCheck
from events.models import EventModel

class AddItemView(CreateView):
	template_name='money_share/add_item_form.html'
	model = MsItemModel
	fields = ['name', 'cost']

	@method_decorator(login_required(login_url = '/loginRequired/'))
	def get(self, request, eventid):
		event = EventModel.getEvent(eventid)
		if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})

		self.eventid=eventid
		return super(AddItemView, self).get(self, request)

	@method_decorator(login_required(login_url = '/loginRequired/'))
	def post(self, request, eventid):
		event = EventModel.getEvent(eventid)
		if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})

		self.eventid=eventid
		return super(AddItemView, self).post(self, request)

	def form_valid(self, form):
		self.success_url = "../"
		form.instance.event_id=self.eventid
		form.instance.purchaser = self.request.user
		return super(AddItemView, self).form_valid(form)

