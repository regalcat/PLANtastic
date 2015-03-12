from django.db import models


class EventModel(models.Model):
	eventid = models.AutoField(primary_key=True)
	eventName = models.CharField(max_length=50)
	eventLocation = models.CharField(max_length=50)
	eventLocation.blank = True
	eventDateStart = models.DateTimeField(auto_now=False,auto_now_add=False)
	eventDateStart.blank = True
	eventType = ('Dinner','Hike','Other Trip','Other Gathering')
	eventDescription = models.CharField(max_length=500)
	eventDescription.blank = True

	def createEvent(self,eventName,eventLocation,eventDateStart,eventType,eventDescription):

		self.eventName=eventName
		self.eventLocation=eventLocation
		self.eventDateStart=eventDateStart
		self.eventType=eventType
		self.eventDescription=eventDescription
		self.save()
		return self

	def getEventTypes(self):
		return ('Dinner', 'Hike', 'Other Trip', 'Other Gathering')

class HikeEventModel(EventModel):
	eventType = 'Hike'
	eventDateEnd = models.DateTimeField(auto_now=False,auto_now_add=False)
	eventDateEnd.blank = True
	eventElevation = models.IntegerField()
	eventElevation.blank = True
	eventDifficulty = ('Unknown','Easy','Moderate','Difficult','Strenuous','Technical')
	eventDistance = models.FloatField()
        eventDistance.blank = True
	eventDuration = models.DateTimeField(auto_now=False,auto_now_add=False)
	eventDuration.blank = True

class GenericTripModel(EventModel):
	eventType = 'Other Trip'
	eventDateEnd = models.DateTimeField(auto_now=False,auto_now_add=False)
	eventDateEnd.blank = True
	eventDuration = models.DateTimeField(auto_now=False,auto_now_add=False)
	eventDuration.blank = True
	eventDestination = models.CharField(max_length=200)
	#should this be TextField? How do we want to implement multidestinations?

class GenericGatheringModel(EventModel):
	eventType = 'Other Gathering'
	eventDateEnd = models.DateTimeField(auto_now=False,auto_now_add=False)
	eventDateEnd.blank = True


	
	
	
        
        
        

