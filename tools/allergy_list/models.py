from django.db import models
from django.contrib.auth.models import User
from events.models import EventModel


class AllergyModel(models.Model):

	CHOICES = ((True, 'Yes'), (False, 'No'))

	user = models.ForeignKey(User)
	event = models.ForeignKey(EventModel)
	vegetarian = models.BooleanField(blank = True, default = False, choices = CHOICES)
	vegan = models.BooleanField(blank = True, default = False, choices = CHOICES)
	lactose = models.BooleanField(blank = True, default = False, choices = CHOICES)
	gluten = models.BooleanField(blank = True, default = False, choices = CHOICES)
	nuts = models.BooleanField(blank = True, default = False, choices = CHOICES)
	other = models.CharField(max_length = 50, blank = True, null = True)


def getCountVegetarian(eventid):
	event = EventModel.objects.filter(eventid=eventid)
	entries = AllergyModel.objects.filter(event=event[0])
	counter = 0
	for entry in entries:
		if entry.vegetarian == True:
			counter += 1
	return counter

def getCountVegan(eventid):
	event = EventModel.objects.filter(eventid=eventid)
	entries = AllergyModel.objects.filter(event=event[0])
	counter = 0
	for entry in entries:
		if entry.vegan == True:
			counter += 1
	return counter

def getCountLactose(eventid):
	event = EventModel.objects.filter(eventid=eventid)
	entries = AllergyModel.objects.filter(event=event[0])
	counter = 0
	for entry in entries:
		if entry.lactose == True:
			counter += 1
	return counter

def getCountGluten(eventid):
	event = EventModel.objects.filter(eventid=eventid)
	entries = AllergyModel.objects.filter(event=event[0])
	counter = 0
	for entry in entries:
		if entry.gluten == True:
			counter += 1
	return counter

def getCountNuts(eventid):
	event = EventModel.objects.filter(eventid=eventid)
	entries = AllergyModel.objects.filter(event=event[0])
	counter = 0
	for entry in entries:
		if entry.nuts == True:
			counter += 1
	return counter
