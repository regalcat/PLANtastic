from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from tools.ride_share.models import *
from events.models import EventModel
from base.helpers import getMenuInfo
from base.permissions import memberCheck
from forms import CarForm, PersonForm
from notifications.models import NotificationModel

@login_required(login_url = '/loginRequired/')
def rideshareindexView(request, eventid):
	event = EventModel.getEvent(eventid)
	user=request.user
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})
	if request.method == 'GET':
		cars = Car.cars.filter(event = event)
		
		isNotInACar=True
		for car in cars:
			car.seats = car.seats
			car.open_seats = car.getOpenSeats(eventid)
			car.passengers.all = car.getPassengerList(eventid)
			if(car.driver.personid == user):
				isNotInACar=False
			elif(car.passengers.filter(personid=user)):
				isNotInACar=False

		context = {'menu' : getMenuInfo(request), 'title' : "Ride Share List", 'isNotInACar':isNotInACar,\
		  'cur_path' : request.get_full_path(), 'cars' : cars, 'event' : event,   }
		return render(request, 'ride_share/main.html', context)

	if request.method == 'POST':
		carid = request.POST['carid']
		return HttpResponseRedirect(reverse('events:tools:rideshare:carDetails', kwargs={'eventid':eventid,'carid':carid}))


@login_required(login_url = '/loginRequired/')
def addCar(request, eventid):
	event = EventModel.getEvent(eventid)
	user = request.user
	
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html')
	if request.method == 'GET':		
		carform = CarForm()

		context = {'menu' : getMenuInfo(request), 'title' : "Add Car", 'carform' : carform, 'event' : event, 'user' : request.user}
		return render(request, 'ride_share/add_car_form.html', context)

	if request.method == 'POST':
		#instance = Car.objects.filter(event = event, user = user)
		#if instance.count() == 0:
		#	carform = CarForm(request.POST)
		#else:
		#	carform = CarForm(request.POST, instance = instance[0])

		carform=CarForm(request.POST)
		
		if carform.is_valid():
			#form = carform.save(commit=False)
			#form.user = request.user
			#form.event = event
			#form.save()
			person=Person(personid=user,status='DR',event=event)
			person.save()
			car=Car(event=event, driver=person, seats=request.POST['seats'], open_seats=request.POST['seats'])
			car.event=event
			car.driver =person
			car.seats = request.POST['seats']
			car.open_seats=car.seats
			car.save()
		return HttpResponseRedirect(reverse('events:tools:rideshare:carDetails', kwargs={'eventid':eventid,'carid':car.carid}))

	
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
	msg = str(request.user)+" joined your car!"
	recipient= car.driver.personid
	note=NotificationModel()
	note.createNewNotification(user=recipient, text=msg)
	return HttpResponseRedirect(reverse('events:tools:rideshare:carDetails', kwargs={'eventid' : eventid,'carid':carid}))



@login_required(login_url = '/loginRequired/')
def carView(request, carid, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	user = request.user
	if memberCheck(request.user, event) == False:
			return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : "Not Member"})
	
	if request.method == 'GET':
		carlist = Car.cars.filter(event=event[0])
		
		isNotInACar=True
		isInThisCar=False
		for car in carlist:
			if(car.passengers.filter(personid=user)):
				isNotInACar=False
			if(car.driver.personid == user):
				isNotInACar=False
		car2 = Car.cars.filter(event=event[0], carid=carid)
		car = car2[0]
		if(car.passengers.filter(personid=user)):
			isInThisCar=True
		passengers = car.getPassengerList(eventid)
		
		car.open_seats = car.getOpenSeats(eventid)
		carid=car.carid
		driver=car.driver
		admin = False
		if (driver.personid == user):
			admin = True
			isNotInACar=False
			
		
		context = {'menu' : getMenuInfo(request), 'title' : "Car Details", 'passengers':passengers, \
				 'eventid' :eventid,'user' : request.user, 'car':car, 'admin':admin, \
				  'driver':driver, 'cur_path' : request.get_full_path(), 'isNotInACar':isNotInACar,\
				'isInThisCar':isInThisCar}
	
		return render(request, 'ride_share/carDetails.html', context)
		
		
	if request.method == 'POST':
		personid = user
		#context['action'] = reverse('events:tools:rideshare:kickPassenger',kwargs={'eventid':eventid, 'carid':carid,'pk':personid, })

		return HttpResponseRedirect(reverse('events:tools:rideshare:kickPassenger', kwargs={'eventid':eventid,\
		 'carid':carid}))


		



@login_required(login_url = '/loginRequired/')
def deleteCar(request, carid, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	eventname=event[0].name
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
	context = {'menu' : getMenuInfo(request), 'title' : "Remove Car", 'eventname':eventname,'car':car, \
		'cur_path':request.get_full_path(),'admin':admin, 'eventid':eventid}
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
	personid = request.POST['personid']
	driver = car.driver
	admin = False
	if car.driver.personid == request.user:
		admin = True
	if memberCheck(request.user, event[0]) == False:
		return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : 'Not Member'})
	if admin == False:
		return render(request, 'events/notPermission.html', {'menu' : getMenuInfo(request), 'title' : 'Not Permission'})
	context = {'menu' : getMenuInfo(request), 'title' : "Remove Passenger from Car", 'admin':admin, 'eventid':eventid,\
			'personid':personid, 'carid':carid}
	return render(request, "ride_share/kickPassenger.html", context)
	#return HttpResponseRedirect(reverse('events:tools:rideshare:executeKick', kwargs={'eventid':eventid,'personid':personid, 'carid':carid}))

	


@login_required(login_url = '/loginRequired/')
def executeKickPassenger(request, carid, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	user = request.POST['personid']
	#personid=request.POST['personid']
	user=User.objects.get(username=request.POST['personid'])
	people = Person.objects.filter(personid=user.id, event=event[0])
	car = Car.cars.get(event=event[0], carid=carid)
	if memberCheck(request.user, event[0]) == False:
		return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : 'Not Member'})
	if car.driver.personid != request.user:
		return render(request, 'events/notPermission.html', {'menu' : getMenuInfo(request), 'title' : 'Not Permission'})
	for person in people:
		car.passengers.remove(person)
		car.save()
		msg = str(car.driver.personid)+" removed you from their car."
		recipient= person.personid
		note=NotificationModel()
		note.createNewNotification(user=recipient, text=msg)
		person.delete()
	return HttpResponseRedirect(reverse('events:tools:rideshare:carDetails', kwargs={'eventid':eventid,'carid':carid}))






@login_required(login_url = '/loginRequired/')
def leaveCar(request, carid, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	user=request.user
	car = Car.cars.get(event=event[0], carid=carid)
	driver=car.driver.personid
	admin = False
	if(car.passengers.filter(personid=user)):
		admin=True
	if memberCheck(request.user, event[0]) == False:
		return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : 'Not Member'})
	if admin==False:
		return render(request, 'events/notPermission.html', {'menu' : getMenuInfo(request), 'title' : 'Not Permission'})

	context = {'menu' : getMenuInfo(request), 'title' : "Leave Car", 'eventid':eventid,'carid':carid, \
		'cur_path':request.get_full_path(), 'driver':driver, 'event':event}
	return render(request, "ride_share/leaveCar.html", context)


@login_required(login_url = '/loginRequired/')
def executeLeaveCar(request, carid, eventid):
	event = EventModel.objects.filter(eventid=eventid)
	user=request.user
	car = Car.cars.get(event=event[0], carid=carid)
	admin = False
	if(car.passengers.filter(personid=user)):
		admin=True
	
	if memberCheck(request.user, event[0]) == False:
		return render(request, 'invite/notMember.html', {'menu' : getMenuInfo(request), 'title' : 'Not Member'})
	if admin == False:
		return render(request, 'events/notPermission.html', {'menu' : getMenuInfo(request), 'title' : 'Not Permission'})
	person=car.passengers.filter(personid=user, event=event)
	car.passengers.remove(person[0])
	car.open_seats +=1
	car.save()
	msg = str(request.user)+" left your car."
	recipient= car.driver.personid
	note=NotificationModel()
	note.createNewNotification(user=recipient, text=msg)
	context = {'menu' : getMenuInfo(request), 'title' : 'Ride Share', 'event':event}
	return HttpResponseRedirect(reverse('events:tools:rideshare:ride_share.index', kwargs={'eventid' : eventid}))
	
