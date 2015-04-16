from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from string import join

#Imported from our code
from event.models import EventModel

class Forum(models.Model):
	title = models.CharField(max_length = 100)
	event = models.ForeignKey(EventModel)

class Thread(models.Model):
	title = models.CharField(max_length = 100)
	created = models.DateTimeField(auto_now_add = True)
	creator = models.ForeignKey(User)
	forum = models.ForeignKey(Forum)

class Post(models.Model):
	title = models.CharField(max_length = 100)
	created = models.DateTimeField(auto_now_add=True)
	creator = models.ForeignKey(User)
	thread = models.ForeignKey(Thread)
	body = models.TextField(max_length=10000)

	def get_post_description(self):
		return u"%s - %s\n%s" % (self.creator, self.title, self.created.strftime("%b %d, %I:%M %p"))


