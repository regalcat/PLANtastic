from django.http import HttpResponse
from django.template import RequestContext, loader
from base.events.models import EventModel

def new(request):
	template = loader.get_template('events/new.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

def details(request, trip_id):
	print "HELLO" # Needed to fix syntax error



