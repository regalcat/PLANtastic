from django.http import HttpResponse

def index(request):
	return HttpResponse("This is the register view.")


def profile(request, userID):
	return HttpResponse("This is the profile of ", userID)








