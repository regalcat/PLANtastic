from django import forms
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import MsItemModel

class AddItemView(CreateView):
	template_name='money_share/add_item_form.html'
	model = MsItemModel
	fields = ['name', 'cost']

	def get(self, request, eventid):
		self.eventid=eventid
		return super(AddItemView, self).get(self, request)

	def post(self, request, eventid):
		self.eventid=eventid
		return super(AddItemView, self).post(self, request)

	def form_valid(self, form):
		self.success_url = "../"
		form.instance.event_id=self.eventid
		form.instance.purchaser = self.request.user
		return super(AddItemView, self).form_valid(form)

