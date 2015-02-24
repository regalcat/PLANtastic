from django.http import HttpResponse
from django.template import RequestContext, loader
from tools.item_share.models import ItemModel

def index(request, eventid):
	template = loader.get_template('item_share/index.html')
	context = RequestContext(request, eventid)
	return HttpResponse(template.render(context))

def form(request, eventid):
	if (request.method == "POST"):
		addItemForm(request, eventid)
	template = loader.get_template('item_share/form.html')
	context = RequestContext(request, {'current_path' : request.get_full_path() })
	return HttpResponse(template.render(context))

def tile(request):
	return HttpResponse("This is the Item-Share Tile.")

def addItemForm(request, event_id):
	print request.POST['itemname']
	item=ItemModel.objects.create(eventid=event_id, item_name=request.POST['itemname'], itemid=0, amount_needed=0, amount_preferred=0)
	item.save()
