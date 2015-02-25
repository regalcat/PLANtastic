## Views.py

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView 
from django.contrib.auth.models import User 
## from django.core.urlresolvers import reverse


def index(request):
	return render(request, 'register/index.html')


def register(request):
	context = {'myPath' : request.get_full_path()}
	return render(request, 'register/register.html', context)	

def profile(request, userID):
	return HttpResponse("This is the profile of " +userID)

def created(request):
	return render(request, 'register/created.html')

class UserCreate(CreateView):
	model = User
	template_name = "register/add.html"
	fields = ['username', 'password', 'first_name', 'last_name', 'email']
	success_url = "created"
	
#	success_url = reverse('created')



#def logIn(request):
	
	

#def createUser(request, ):
#	user = 
#
#	user.Save()
















