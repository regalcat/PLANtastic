from django.contrib.auth.models import User
from django.db import models

from events.models import EventModel

class FriendList(models.Model):
	user = models.ForeignKey(User,primary_key=True)
	friends = models.ManyToManyField(User, related_name='friends')
	
	def getFriendList(user_):
		friends = FriendList.objects.get(user=user_)
		friendlist = ""
		for user in friends:
			friendlist += user.username
		return friendlist
