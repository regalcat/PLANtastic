from django.db import models

class EventModel(models.Model):
	eventid = models.AutoField(primary_key=True)
	eventName = models.CharField(max_length=50)
	eventLocation = models.CharField(max_length=50)
	eventLocation.blank = True
	eventDateStart = models.DateTimeField(auto_now=False,auto_now_add=False)
	#eventDateStart.blank = True
	# TODO - Use actual enum type.
	eventTypes = ('Dinner', 'Hike', 'Other Trip', 'Other Gathering')
	eventType = 'Other Gathering'
	eventDescription = models.CharField(max_length=500)
	eventDescription.blank = True

	#Base template for showing the event description.
	eventDescriptionTemplate = 'events/base_description.html'

	def createEvent(self,eventName,eventLocation,eventDateStart,eventType,eventDescription):
		self.eventName=eventName
		self.eventLocation=eventLocation
		self.eventDateStart=eventDateStart
		self.eventType=eventType
		self.eventDescription=eventDescription
		self.save()
		return self

	@staticmethod
	def getEventTypes():
		return ('Dinner', 'Hike', 'Other Trip', 'Other Gathering')

class HikeEventModel(EventModel):
	
	eventType = 'Hike'
	eventDateEnd = models.DateTimeField(auto_now=False,auto_now_add=False)
	eventDuration = models.CharField(max_length=30, blank=True)
	eventElevation = models.IntegerField(blank=True, null=True)
	eventDistance = models.FloatField(blank=True, null=True)
	eventDifficulty = ('Unknown','Easy','Moderate','Difficult','Strenuous','Technical')
    
	#Template for the description about the trip.
	eventDescriptionTemplate = 'events/hike_description.html'



class GenericTripModel(EventModel):
	eventType = 'Other Trip'
	eventDateEnd = models.DateTimeField(auto_now=False,auto_now_add=False)
	eventDateEnd.blank = True
	eventDuration = models.DateTimeField(auto_now=False,auto_now_add=False)
	eventDuration.blank = True
	eventDestination = models.CharField(max_length=200)
	#should this be TextField? How do we want to implement multidestinations?

	#Template for the description about the trip.
	eventDescriptionTemplate = 'events/generic_description.html'

class GenericGatheringModel(EventModel):
	eventType = 'Other Gathering'
	eventDateEnd = models.DateTimeField(auto_now=False,auto_now_add=False)
	eventDateEnd.blank = True

	eventDescriptionTemplate = 'events/other_description.html'

class InviteModel(models.Model):
	inviteID = models.AutoField(primary_key=True)
	inviteEvent = models.ForeignKey(EventModel)
	inviteEmail = models.CharField(max_length=60)
