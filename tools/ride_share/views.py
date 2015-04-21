from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from tools.ride_share.models import *
from events.models import EventModel
from base.helpers import getMenuInfo
from base.permissions import memberCheck
from forms import CarForm, PersonForm

@login_required(login_url = '/loginRequired/')
def rideshareindexView(request, eventid):
	event = EventModel.getEvent(eventid)
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})

	cars = Car.cars.filter(event = event)
	

	for car in cars:
		#for passenger in car.passengers.all():
			#if (passenger.status == 'DR'):
				#car.driver = passenger
		car.seats = car.seats
		car.open_seats = car.getOpenSeats(eventid)
		car.passengers.all = car.getPassengerList(eventid)
		
	context = {'menu' : getMenuInfo(request), 'title' : "Ride Share List", 'cars' : cars, 'event' : event,   }
	return render(request, 'ride_share/main.html', context)

@login_required(login_url = '/loginRequired/')
def addCar(request, eventid):
	event = EventModel.getEvent(eventid)
	user = request.user
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html')
	if request.method == 'GET':
		instance = Car.objects.filter(event = event, user = user)
		if instance.count() == 0:
			carform = CarForm()
		else:
			carform = CarForm(instance = instance[0])

		context = {'menu' : getMenuInfo(request), 'title' : "Add Car", 'carform' : carform, 'event' : event, 'user' : request.user}
		return render(request, 'ride_share/addCar.html', context)

	if request.method == 'POST':
		instance = Car.objects.filter(event = event, user = user)
		if instance.count() == 0:
			carform = CarForm(request.POST)
		else:
			carform = CarForm(request.POST, instance = instance[0])

		
		if carform.is_valid():
			form = carform.save(commit=False)
			form.user = request.user
			form.event = event
			form.save()
		return HttpResponseRedirect(reverse('events:tools:rideshare:addCar', kwargs={'eventid' : eventid}))

	
@login_required(login_url = '/loginRequired/')
def signupView(request, eventid):
	event = EventModel.getEvent(eventid)
	user = request.user
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html')
	if request.method == 'GET':
		instance = Car.cars.filter(event = event)
		if instance.count() == 0:
			personform = PersonForm()
		else:
			personform = PersonForm(instance = instance[0])

		context = {'menu' : getMenuInfo(request), 'title' : "Choose A Car", 'personform' : personform, 'event' : event, 'user' : request.user}
		return render(request, 'ride_share/signup.html', context)

	if request.method == 'POST':
		instance = Car.cars.filter(event = event, user = user)
		if instance.count() == 0:
			personform = PersonForm(request.POST)
		else:
			personform = PersonForm(request.POST, instance = instance[0])

		
		if personform.is_valid():
			form = personform.save(commit=False)
			form.user = request.user
			form.event = event
			form.save()
		return HttpResponseRedirect(reverse('events:tools:rideshare:signup', kwargs={'eventid' : eventid}))

	

	
