from django.contrib.auth.models import User
from django.db import models

from base.events.models import EventModel, InviteModel

class MembershipModel(models.Model):
	CREATOR = 'CR'
	COPLANNER = 'CP'
	MEMBER = 'MEM'
	STATUSES = (
		(CREATOR, 'CREATOR'),
		(COPLANNER, 'COPLANNER'),
		(MEMBER, 'MEMBER')
	)
	event = models.ForeignKey(EventModel)
	user = models.ForeignKey(User)
	status = models.CharField(max_length=3, choices=STATUSES)
