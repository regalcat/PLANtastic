from django.http import HttpResponse
from django.template import RequestContext, loader

from django.contrib.auth.models import User
from base.Helpers import getUser, getEvent, getMenuInfo
from base.events.models import EventModel
from tools.item_share.models import ItemModel, ItemSignupModel
from tools.ToolView import ToolView

class ItemShareView(ToolView):
	def getTileTemplate():
		return ("item_share/tile.html")
	
	def getMainPageUrl():
		return "item_share"

	def get(self, request, eventid):
		user = getUser(request)
		cur_event = getEvent(eventid)
		items = ItemModel.items.filter(id=1)
		for item in items:
			item.signups = ItemSignupModel.objects.filter(itemid = item)
			item.signedup = 0
			for signup in item.signups:
				item.signedup += signup.amount
		admin = False
#		if (user.isCoPlanner(event) or user.isCreator(event)):
		if (True):
			admin = True
		template = loader.get_template("item_share/main.html")
		context = RequestContext(request, {'items' : items, 'event' : cur_event, 'user' : user, 'cur_path' : request.get_full_path(), 'title' : "Item Share", 'menu': getMenuInfo(request) })
		return HttpResponse(template.render(context))

	def post(request, eventid):
		
		print request.POST['amount']
		print request.POST['item_id']
		print request.POST['uid']
		print request.POST['event_id']
		return HttpResponse("Post Item Share page")
