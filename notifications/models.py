from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class NotificationModel(models.Model):

	user = models.ForeignKey(User)
	time = models.DateTimeField()
	text = models.CharField(max_length = 10000)
	seen = models.BooleanField(default = False)
	link = models.CharField(max_length = 10000, blank = True)
	btnText = models.CharField(max_length = 100, blank=True)
	eventarg = models.IntegerField(blank=True, null = True)
	friendarg = models.IntegerField(blank=True, null = True)



	def createNewNotification(self, user, text):
		self.user = user
		self.time = timezone.now()
		self.text = text
		self.seen = False
		self.save()
		return self

	def createButtonNotification(self, user, text, link, btnText, eventarg, friendarg):
		self.user = user
		self.time = timezone.now()
		self.text = text
		self.seen = False
		self.link = link
		self.btnText = btnText
		self.eventarg = eventarg
		self.friendarg = friendarg
		self.save()
		return self


