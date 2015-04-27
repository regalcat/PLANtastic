from django.db import models
from django.contrib.auth.models import User

from events.models import EventModel

def getUploadDir(instance, filename):
	return "uploads/event_pics/" + str(instance.event.eventid) + "/" + filename

class UploadedPicModel(models.Model):
	event = models.ForeignKey(EventModel)
	caption = models.CharField(max_length=200, blank=True, null=True)
	file = models.ImageField(upload_to=getUploadDir)
	uploader = models.ForeignKey(User)
	title = models.CharField(max_length=50)

