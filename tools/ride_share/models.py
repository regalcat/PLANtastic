from django.db import models
from django.contrib.auth.models import User
from events.models import EventModel
from django.contrib.auth.models import User

from users import forms as userForms


class RideModel(models.Model):
	rideid = models.AutoField(primary_key=True)
	event = models.ForeignKey(EventModel)
	seats = models.IntegerField()
	cars = models.Manager()
	driver = models.CharField(max_length = 25)



class RideSignupModel(models.Model):
	DRIVER = 'DR'
	PASSENGER = 'PS'
	STATUSES = (
		(DRIVER, 'Driver'),
		(PASSENGER, 'Passenger'),
	)	
	event = models.ForeignKey(EventModel)
	user = models.ForeignKey(User)
	rideid = models.ForeignKey(RideModel)
	status = models.CharField(max_length=3, choices=STATUSES)
	address = models.CharField(max_length=50)
	objects = models.Manager()
