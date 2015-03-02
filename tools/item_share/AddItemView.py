from django import forms
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from tools.item_share.models import ItemModel

class AddItemView(CreateView):
	template_name='item_share/add_item_form.html'
	model = ItemModel
	fields = ['item_name', 'amount_needed', 'amount_preferred']

	def get(self, request, eventid):
		self.eventid=eventid
		return super(AddItemView, self).get(self, request)

	def post(self, request, eventid):
		self.eventid=eventid
		return super(AddItemView, self).post(self, request)

	def form_valid(self, form):
		self.success_url = "http://"+self.request.get_host()+"/"+self.eventid+"/tools/item_share"
		form.instance.event_id=self.eventid
		return super(AddItemView, self).form_valid(form)

		#self.object = form.save(commit=False)
		#self.object.event_id=self.eventid
		#self.object.save()
		#return HttpResponseRedirect("http://192.168.56.102/home")
