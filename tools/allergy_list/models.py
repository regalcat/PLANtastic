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
	
