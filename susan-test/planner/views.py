from django.http import HttpResponse

def hello(request):
	print 'Hello'
	return HttpResponse("Hello world")
