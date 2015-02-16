from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

def base(request):
	template = loader.get_template('base.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))
