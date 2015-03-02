from django.http import HttpResponse
from django.template import RequestContext, loader

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from base.Helpers import getEvent, getMenuInfo
from base.events.models import EventModel
from tools.item_share.models import ItemModel, ItemSignupModel
from tools.ToolView import ToolView

class ItemShareView(ToolView):
	def getTileTemplate():
		return ("item_share/tile.html")
	
	def getMainPageUrl():
		return "item_share"

	def get(self, request, eventid):
		user = request.user
		cur_event = getEvent(eventid)
		items = ItemModel.items.filter(event=cur_event)
		for item in items:
			item.signups = ItemSignupModel.objects.filter(itemid = item).exclude(user=request.user)
			item.your_signup = ItemSignupModel.objects.filter(itemid=item, user=request.user)
			item.signedup = 0
			for signup in item.signups:
				item.signedup += signup.amount
			if item.your_signup.count() == 0:
				item.your_signup = False
			else:
				item.your_signup = item.your_signup[0]
				item.signedup += item.your_signup.amount
		admin = False
#		if (user.isCoPlanner(event) or user.isCreator(event)):
		if (True):
			admin = True
		template = loader.get_template("item_share/main.html")
		context = RequestContext(request, {'items' : items, 'event' : cur_event, 'cur_path' : request.get_full_path(), 'title' : "Item Share", 'menu': getMenuInfo(request) })
		return HttpResponse(template.render(context))

	@csrf_exempt
	def post(self, request, eventid):		
		ajax = request.POST.get('ajax', False)
		cur_event=getEvent(eventid)
		item = ItemModel.items.get(id=request.POST['item_id'], event=cur_event)
		signup = ItemSignupModel.objects.update_or_create(itemid=item, user = request.user, event=cur_event, defaults={'amount' : request.POST['amount']})
		if ajax:
			# TODO - return sum of all people brining
			items = ItemSignupModel.objects.filter(itemid=item, event=cur_event)
			total = 0
			for item in items:
				total += item.amount
			return HttpResponse(total)
		return self.get(request, eventid)
