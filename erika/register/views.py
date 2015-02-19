from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return render(request, 'register/index.html')


def register(request):
	context = {'myPath' : request.get_full_path()}
	return render(request, 'register/register.html', context)	

def profile(request, userID):
	return HttpResponse("This is the profile of " +userID)








