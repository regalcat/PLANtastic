from django import forms
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from tools.item_share.models import ItemModel

class AddItemForm(FormView):
	item_name = forms.CharField()
	amount_needed = forms.IntegerField()
	amount_preferred = forms.IntegerField()

	def print_test(self):
		print item_name + " " + amount_needed + " " + amount_preferred

class AddItemView(CreateView):
	template_name='item_share/add_item_form.html'
	model = ItemModel
	fields = ['item_name', 'amount_needed', 'amount_preferred']

