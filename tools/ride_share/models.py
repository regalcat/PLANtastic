from django.db import models
from django.contrib.auth.models import User
from events.models import EventModel
from django.contrib.auth.models import User

from users import forms as userForms


class Person(models.Model):
	
	DRIVER = 'DR'
	PASSENGER = 'PS'
	STATUSES = (
		(DRIVER, 'Driver'),
		(PASSENGER, 'Passenger'),
	)	
	event = models.ForeignKey(EventModel)
	personid = models.ForeignKey(User)
	status = models.CharField(max_length=3, choices=STATUSES)
	address = models.CharField(max_length=50)

	
	def newPerson(self,event, personid, status):
		self.event=event
		self.personid=personid
		self.status=status
		self.save()
		return self



class Car(models.Model):
	carid = models.AutoField(primary_key=True)
	event = models.ForeignKey(EventModel)
	seats = models.IntegerField()
	cars = models.Manager()
	event = models.ForeignKey(EventModel)
	passengers = models.ManyToManyField(Person)
	open_seats = models.IntegerField(default=0)
	driver = models.ForeignKey(Person, related_name='driver')


	def getOpenSeats(self, eventid):
		event = EventModel.objects.filter(eventid=eventid)
		car = Car.cars.get(event=event[0], carid=self.carid)
		open_seats = (int)(car.seats-car.passengers.count())
		return open_seats

	def getPassengerList(self, eventid):
		event = EventModel.objects.filter(eventid=eventid)
		car = Car.cars.get(event=event[0], carid=self.carid)
		return car.passengers

	def newCar(self, event, seats, driver):
		self.event=event
		self.seats=seats
		self.open_seats = seats
		self.driver = driver
		self.save()
		return self


class Riders(models.Model):
	car = models.ForeignKey(Car)
	person = models.ForeignKey(Person)
		


