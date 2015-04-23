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
		car.seats = car.seats
		car.open_seats = car.getOpenSeats(eventid)
		car.passengers.all = car.getPassengerList(eventid)

	context = {'menu' : getMenuInfo(request), 'title' : "Ride Share List",  'cur_path' : request.get_full_path(), \
			'cars' : cars, 'event' : event,   }
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
		return HttpResponseRedirect(reverse('events:tools:rideshare', kwargs={'eventid' : eventid}))

	
@login_required(login_url = '/loginRequired/')
def signupView(request, carid, eventid):
	event = EventModel.getEvent(eventid)
	user = request.user
	car = Car.cars.get(event=event, carid=carid)
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html')
	if request.method == 'GET':
		instance = Person.objects.filter(event=event, personid=user)
		if instance.count() == 0:
			personform = PersonForm()
		else:
			personform = PersonForm(instance = instance[0])

		context = {'menu' : getMenuInfo(request), 'title' : "Sign Up", 'personform' : personform, 'event' : event, 'user' : request.user}
		return render(request, 'ride_share/sign_up_form.html', context)

	if request.method == 'POST':
		instance = Car.cars.car(event = event,carid=carid)
		if instance.count() == 0:
			personform = PersonForm(request.POST)
		else:
			personform = PersonForm(request.POST, instance = instance[0])

		 
		if personform.is_valid():
			form = personform.save(commit=False)
			form.user = request.user
			form.event = event
			form.save()
			
		return HttpResponseRedirect(reverse('events:tools:rideshare:executeSignup', kwargs={'eventid':eventid, 'carid':carid}))


@login_required(login_url = '/loginRequired/')
def executeSignup(request, carid, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	if memberCheck(request.user, event) == False:
		return render(request, 'invite/notMember.html')
	person=Person(personid=request.user, event=event[0], address=request.POST['address'])
	person.save()
	#person = Person.objects.get(personid=request.user, event=event)
	car = Car.cars.get(event=event[0], carid=carid)
	car.passengers.add(person)
	car.open_seats -= 1
	car.save()
	return HttpResponseRedirect(reverse('events:tools:rideshare:carDetails', kwargs={'eventid' : eventid,'carid':carid}))



@login_required(login_url = '/loginRequired/')
def carView(request, carid, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	user = request.user
	car = Car.cars.get(event=event[0], carid=carid)

	passengers = car.getPassengerList(eventid)

	car.open_seats = car.getOpenSeats(eventid)
	if request.method == 'GET':
		
		driver=car.driver
		admin = False
		if (driver.personid == user):
			admin = True
		context = {'menu' : getMenuInfo(request), 'title' : "Car Details", 'passengers':passengers, \
				 'eventid' :eventid,'user' : request.user, 'car':car, 'admin':admin, \
				  'driver':driver, 'cur_path' : request.get_full_path()}
	
		return render(request, 'ride_share/carDetails.html', context)

	if request.method == 'POST':
		personid= person.personid
		#context['action'] = reverse('events:tools:rideshare:kickPassenger',kwargs={'eventid':eventid, 'carid':carid,'pk':personid, })

		return HttpResponseRedirect(reverse('events:tools:rideshare:kickPassenger', kwargs={'eventid':eventid,\
		 'carid':carid, 'pk':personid}))


		



@login_required(login_url = '/loginRequired/')
def deleteCar(request, carid, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	car = Car.cars.get(event=event[0], carid=carid)
	user=request.user
	driver = car.driver.personid
	admin = False
	if driver == user:
		admin = True
	if memberCheck(request.user, event[0]) == False:
		return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : 'Not Member'})
	if admin == False:
		return render(request, 'events/notPermission.html', {'menu' : getMenuInfo(request), 'title' : 'Not Permission'})
	context = {'menu' : getMenuInfo(request), 'title' : "Remove Car", 'eventid':eventid,'car':car, \
		'cur_path':request.get_full_path(),'admin':admin, 'event':event}
	return render(request, "ride_share/deleteCar.html", context)


@login_required(login_url = '/loginRequired/')
def executeDeleteCar(request, carid, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	car = Car.cars.get(event=event[0], carid=carid)
	if memberCheck(request.user, event[0]) == False:
		return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : 'Not Member'})
	if car.driver.personid != request.user:
		return render(request, 'events/notPermission.html', {'menu' : getMenuInfo(request), 'title' : 'Not Permission'})

	car.delete()
	
	context = {'menu' : getMenuInfo(request), 'title' : 'Ride Share', 'event':event}
	return HttpResponseRedirect(reverse('events:tools:rideshare:ride_share.index', kwargs={'eventid' : eventid}))

	
@login_required(login_url = '/loginRequired/')
def kickPassenger(request, carid, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	car = Car.cars.get(event=event[0], carid=carid)
	driver = car.driver
	admin = False
	if car.driver.personid == request.user:
		admin = True
	if memberCheck(request.user, event[0]) == False:
		return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : 'Not Member'})
	if admin == False:
		return render(request, 'events/notPermission.html', {'menu' : getMenuInfo(request), 'title' : 'Not Permission'})
	context = {'menu' : getMenuInfo(request), 'title' : "Remove Passenger from Car", 'admin':admin, 'event':event}
	return render(request, "ride_share/kickPassenger.html", context)
	#return HttpResponseRedirect(reverse('events:tools:rideshare:executeKick', kwargs={'eventid':eventid,'personid':personid, 'carid':carid}))


@login_required(login_url = '/loginRequired/')
def executeKickPassenger(request, carid, personid, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	person = Person.objects.filter(personid=personid, event=event[0])
	car = Car.cars.get(event=event[0], carid=carid)
	if memberCheck(request.user, event[0]) == False:
		return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : 'Not Member'})
	if car.driver.personid != request.user:
		return render(request, 'events/notPermission.html', {'menu' : getMenuInfo(request), 'title' : 'Not Permission'})
	
	car.passengers.remove(person)
	car.save()
	person.delete()
	
	return HttpResponseRedirect(reverse('events:tools:rideshare:carView', kwargs={'eventid':eventid,'carid':carid}))

	
