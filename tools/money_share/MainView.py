from django.shortcuts import redirect, render
from django.views.generic import View

from base.helpers import getMenuInfo
from events.models import EventModel
from invite.models import MembershipModel
from settings import settings

from .models import MsItemModel, MsPaymentModel, MsSettingsModel

class MainView(View):
	template_name = "money_share/index.html"

	def get(self, request, eventid):
		if MsSettingsModel.objects.filter(event = eventid).count() == 0:
			MsSettingsModel(event_id=eventid, method=MsSettingsModel.EQUAL).save()
		items = MsItemModel.objects.filter(event = eventid)
		payments = MsPaymentModel.objects.filter(event = eventid)
		method = MsSettingsModel.objects.get(event = eventid)
		members = MembershipModel.objects.filter(event=eventid)
		amounts = {}
		for member in members:
			amounts[str(member.id)] = {}
			amounts[str(member.id)]['userinfo'] = member
			amounts[str(member.id)]['owe'] = 0
			amounts[str(member.id)]['spent'] = 0
			amounts[str(member.id)]['paid'] = 0
			amounts[str(member.id)]['received'] = 0
		if method.method == MsSettingsModel.EQUAL:
			method.method = "Equal"
			sum = 0;
			for item in items:
				sum += item.cost
				amounts[str(item.purchaser.id)]['spent'] += item.cost
			temp = sum/members.count()
			for person in amounts:
				person['owe'] = temp
		elif method.method == MsSettingsModel.ITEM_BY_ITEM:
			method.method = "Item By Item"
			for item in items:
				#TODO - Split cost By who's on the item
				amounts[str(item.purchaser.id)]['spent'] += item.cost
		
		for payment in payments:
			amounts[str(payment.payer.id)]['paid'] += payment.amount
			amounts[str(payment.receiver.id)]['received'] += payment.amount
		print amounts
		for index in amounts:
			person = amounts[index]
			person['total'] = -1*(person['owe'] - person['spent'] - person['paid'] + person['received'])
		return render(request, self.template_name, \
			{'menu' : getMenuInfo(request), 'title' : "Upload Pics Tool", \
				'items' : items, 'payments' : payments, 'method' : method, \
				'amounts' : amounts})

	def post(self, request, eventid):
		return redirect("edit_pic/"+str(pic.id))
