from django.db import models
from django.contrib.auth.models import User
from events.models import EventModel
from django.contrib.auth.models import User

from users import forms as userForms


class Gmap(models.Model):
	
	mapid= models.AutoField(primary_key=True)
	event = models.ForeignKey(EventModel)

	location = models.CharField(max_length=100)

	
	def newGmap(self,event, location):
		self.event=event
		self.location=location
		self.save()
		return self


