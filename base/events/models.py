from django.db import models

class EventModel(models.Model):
	eventid = models.AutoField(primary_key=True)
	eventName = models.CharField(max_length=50)
	eventLocation = models.CharField(max_length=50)
	eventLocation.blank = True
	eventDateStart = models.DateTimeField(auto_now=False,auto_now_add=False)
	eventDateStart.blank = True
	# TODO - Use actual enum type.
	eventTypes = ('Dinner', 'Hike', 'Other Trip', 'Other Gathering')
	eventType = 'Other Gathering'
	eventDescription = models.CharField(max_length=500)
	eventDescription.blank = True

	#Base template for showing the event description.
	eventDescriptionTemplate = 'events/base_description.html'

	# Returns the event that is currently in play from the event_id
	@staticmethod
	def getEvent(event_id):
		events = HikeEventModel.objects.filter(eventid=event_id)
		if (events.count() == 1):
			return events[0]
		events = GenericTripModel.objects.filter(eventid=event_id)
		if (events.count == 1):
			return events[0]
		events = GenericGatheringModel.objects.filter(eventid=event_id)
		if events.count == 1:
			return events[0]
		return EventModel.objects.get(eventid=event_id)

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
	eventDateEnd.blank = True
	eventElevation = models.IntegerField()
	eventElevation.blank = True
	eventDifficulty = ('Unknown','Easy','Moderate','Difficult','Strenuous','Technical')
	eventDistance = models.FloatField()
        eventDistance.blank = True
	eventDuration = models.DateTimeField(auto_now=False,auto_now_add=False)
	eventDuration.blank = True
    
	#Template for the description about the trip.
	eventDescriptionTemplate = 'events/hike_description.html'

	def createEvent(self, eventName, eventLocation, eventDateStart, eventType, eventDescription, eventDateEnd, eventElevation, eventDifficulty, eventDistance, eventDuration):
		super(HikeEventModel, self).__init__(eventName, eventLocation, eventDateStart, eventType, eventDescription)
		self.eventDateEnd = eventDateEnd
		self.eventElevation = eventElevation
		self.eventDifficulty = eventDifficulty
		self.eventDistance = eventDistance
		self.eventDuration = eventDuration
		self.save()
		return self

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
