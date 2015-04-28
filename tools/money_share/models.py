from django.db import models
from django.contrib.auth.models import User
from events.models import EventModel
from invite.models import MembershipModel

class MsSettingsModel(models.Model):
	EQUAL = 'E'
	ITEM_BY_ITEM = 'I'
	METHODS = (
		(EQUAL, 'Equal'),
		(ITEM_BY_ITEM, 'Item By Item'),
	)
	event = models.ForeignKey(EventModel)
	method = models.CharField(max_length=1, choices=METHODS)

class MsItemModel(models.Model):
	name = models.CharField(max_length=10)
	cost = models.IntegerField()
	purchaser = models.ForeignKey(User)
	event = models.ForeignKey(EventModel)

# If item-by-item sharing method is used, the list below stores who will share te cost of an item.
# If no entry found here, then cost will be shared equally among all members of trip.
class MsSplitsModel(models.Model):
	item = models.ForeignKey(MsItemModel)
	event = models.ForeignKey(EventModel)
	user = models.ForeignKey(User)

	@staticmethod
	def getUsersSplitting(event_, item_):
		if MsSettingsModel.ITEM_BY_ITEM == MsSettingsModel.objects.get(event=event_).method:
			users = MsSplitsModel.objects.filter(item = item_, event = event_).values_list( \
				'user', flat=True)
			users = list(users)
			users.append(item_.purchaser)
		else:
			users = MembershipModel.objects.filter(event=event_).values_list( \
				'user', flat=True)
		return users

class MsPaymentModel(models.Model):
	payer = models.ForeignKey(User, related_name='payer')
	receiver = models.ForeignKey(User, related_name='receiver')
	amount = models.IntegerField()
	event = models.ForeignKey(EventModel)
