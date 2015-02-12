from django.http import HttpResponse

def index(request, eventid):
	return HttpResponse("Welcome to the main Item-Share webpage. Your trip id is "+eventid)

def tile(request):
	return HttpResponse("This is the Item-Share Tile.")

def addItemForm(request):
	return HttpResponse("This is the Add Item form.")
