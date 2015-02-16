from django.http import HttpResponse
from django.template import RequestContext, loader
from events.models import EventModel

def index(request):
	template = loader.get_template('new_event/index.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

def details(request, trip_id):
	


