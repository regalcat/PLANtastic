from django.db import models

class ItemSignupModel(models.Model):
	eventid = models.ForeignKey(EventModel)
	uid = models.ForeignKey(UserModel)
	itemid = models.ForeignKey(ItemModel)
	amount = IntegerField()

class ItemModel(models.Model):
	eventid = models.ForeignKey(EventModel)
	itemid = models.IntegerField(primary_key=True)
	item_name = models.CharFild(maxLength=50)
	amount_needed = models.IntegerField()
	amount_preferred = models.IntegerField()

