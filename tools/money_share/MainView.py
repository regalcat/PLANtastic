from django.shortcuts import redirect, render
from django.views.generic import View

from base.helpers import getMenuInfo
from events.models import EventModel
from settings import settings

from .models import MsItemModel, MsPaymentModel

class MainView(View):
	template_name = "money_share/index.html"

	def get(self, request, eventid):
		items = MsItemModel.objects.filter(event = eventid)
		payments = MsPaymentModel.objects.filter(event = eventid)
		return render(request, self.template_name, \
			{'menu' : getMenuInfo(request), 'title' : "Upload Pics Tool", \
				'items' : items, 'payments' : payments})

	def post(self, request, eventid):
		return redirect("edit_pic/"+str(pic.id))
