from django.db import models
#from base.models import EventModel
#from base.models import UserModel

class ItemModel(models.Model):
# TODO - Get EventModel from Megan
#	eventid = models.ForeignKey(EventModel)
	eventid = models.IntegerField()
	itemid = models.IntegerField(primary_key=True)
	item_name = models.CharField(max_length=50)
	amount_needed = models.IntegerField()
	amount_preferred = models.IntegerField()

class ItemSignupModel(models.Model):
#	eventid = models.ForeignKey(EventModel)
#o	uid = models.ForeignKey(UserModel)
	itemid = models.ForeignKey(ItemModel)
	amount = models.IntegerField()
