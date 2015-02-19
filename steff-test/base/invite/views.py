from django.http import HttpResponse
from django.template import RequestContext, loader

def test(request):
	template = loader.get_template('index.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))


