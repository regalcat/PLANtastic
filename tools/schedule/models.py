from django.db import models
from events.models import EventModel


class ScheduleModel(models.Model):

	scheduleid = models.AutoField(primary_key=True)
	event = models.ForeignKey(EventModel)
	name = models.CharField(max_length = 50)
	description = models.CharField(max_length=300, blank = True)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField(blank=True, null=True)
	

	def createActivity(self, event, name, description, start_date, end_date):
		self.event = event
		self.name = name
		self.description = description
		self.start_date = start_date
		self.end_date = end_date
		self.save()
		return self

