from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class NotificationModel(models.Model):

	user = models.ForeignKey(User)
	time = models.DateTimeField()
	text = models.CharField(max_length = 10000)
	seen = models.BooleanField(default = False)


	def createNewNotification(self, user, text):
		self.user = user
		self.time = timezone.now()
		self.text = text
		self.seen = False
		self.save()
		return self

