from tools.ToolView import ToolView
from models import *

class MoneyShareTool(ToolView):
	tile_template = "money_share/money_share_tile.html"

	@staticmethod
	def getIdentifier():
		return "money_share"


	@staticmethod
	def getContext(event):
		eventid=event.eventid
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
				amounts[person]['owe'] = temp
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
		context={'items' : items, 'amounts' : amounts, 'members':members}
		return context
