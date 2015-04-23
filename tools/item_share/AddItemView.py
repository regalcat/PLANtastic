from django import forms
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from tools.item_share.models import ItemModel
from events.models import EventModel
from base.permissions import memberCheck


class AddItemView(CreateView):
	template_name='item_share/add_item_form.html'
	model = ItemModel
	fields = ['item_name', 'amount_needed', 'amount_preferred']

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
		self.success_url = "http://"+self.request.get_host()+"/"+self.eventid+"/tools/item_share"
		form.instance.event_id=self.eventid
		return super(AddItemView, self).form_valid(form)

