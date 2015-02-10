from django.db import models

class EventModel(models.Model):
	eventid = models.IntegerField(primary_key=True)

class UserModel(models.Model):
	itemid = models.IntegerField(primary_key=True)
