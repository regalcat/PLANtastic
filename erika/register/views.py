## Views.py

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse


def index(request):
	return render(request, 'register/index.html')


def register(request):
	context = {'myPath' : request.get_full_path()}
	return render(request, 'register/register.html', context)	

def profile(request, user):
	return HttpResponse("This is the profile of " +user)

def created(request):
	return render(request, 'register/created.html')

def myLogin(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)

	if user is not none:
		login(request, user)
		#redirect to success page
		return httpResponseRedirect(reverse(register:profile),  )
	else:
		# Invalid login
		return render(request, )

def myLogout(request):
	logout(request)
	# redirect to sucesspage (home? index?)
		
		


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
















