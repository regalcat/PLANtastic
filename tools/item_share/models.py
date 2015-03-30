from django.db import models
from django.contrib.auth.models import User
from base.events.models import EventModel

class ItemModel(models.Model):
	event = models.ForeignKey(EventModel)
	item_name = models.CharField(max_length=50)
	amount_needed = models.IntegerField()
	amount_preferred = models.IntegerField()
	items=models.Manager()

class ItemSignupModel(models.Model):
	event = models.ForeignKey(EventModel)
	user = models.ForeignKey(User)
	itemid = models.ForeignKey(ItemModel)
	amount = models.IntegerField()
	objects = models.Manager()
