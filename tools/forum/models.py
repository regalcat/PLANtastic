from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from string import join

#Imported from our code
from events.models import EventModel

class ForumModel(models.Model):
	title = models.CharField(max_length = 100)
	event = models.ForeignKey(EventModel)
	forums = models.Manager()

class ThreadModel(models.Model):
	threadid = models.AutoField(primary_key=True)
	title = models.CharField(max_length = 100)
	created = models.DateTimeField(auto_now_add = True)
	creator = models.ForeignKey(User)
	forum = models.ForeignKey(ForumModel)
	body = models.TextField(max_length=10000)
	threads = models.Manager()

	def num_posts(self):
		return PostModel.posts.filter(thread=self).count()

	def last_post(self):
		posts = PostModel.posts.filter(thread=self)
		if posts.count() > 0:
			return posts.order_by("created")[0]

class PostModel(models.Model):
	title = models.CharField(max_length = 100)
	created = models.DateTimeField(auto_now_add=True)
	creator = models.ForeignKey(User)
	thread = models.ForeignKey(ThreadModel)
	body = models.TextField(max_length=10000)
	posts = models.Manager()

	def get_post_description(self):
		return u"%s - %s\n%s" % (self.creator, self.title, self.created.strftime("%b %d, %I:%M %p"))


