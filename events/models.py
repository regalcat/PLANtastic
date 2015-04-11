from django.db import models

class EventModel(models.Model):
	eventid = models.AutoField(primary_key=True)
	eventName = models.CharField(max_length=50)
	eventLocation = models.CharField(max_length=50)
	eventLocation.blank = True
	eventDateStart = models.DateField(auto_now=False,auto_now_add=False)
	#eventDateStart.blank = True
	
	EVENT_TYPES = (
		('Dinner', 'Dinner'), 
		('Hike', 'Hike'), 
		('Other Trip', 'Other Trip'),
		('Other Gathering', 'Other Gathering'),
	)

	
	eventType = models.CharField(max_length=20, choices=EVENT_TYPES, blank=False, default=None)
	eventDescription = models.CharField(max_length=500)
	eventDescription.blank = True
	eventType.default = None
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
	LEVELS = (('unknown', 'Unknown'), ('easy', 'Easy'), ('moderate', 'Moderate'), ('difficult', 'Difficult'),
	('strenuous', 'Strenuous'), ('technical', 'Technical'),)
	
	eventType = 'Hike'
	eventDateEnd = models.DateTimeField(auto_now=False,auto_now_add=False, blank=True, null=True)
	eventDuration = models.CharField(max_length=30, blank=True)
	eventElevation = models.IntegerField(blank=True, null=True)
	eventDistance = models.FloatField(blank=True, null=True)

	#EVENT_DIFFICULTIES= (
	#	('unknown', 'Unknown'),
	#	('easy', 'Easy'),
	#	('moderate', 'Moderate'),
	#	('difficult', 'Difficult'),
	#	('strenuous', 'Strenuous'),
	#	('technical', 'Technical'),
	#)
	#eventDifficulty = models.CharField(max_length=9, choices=EVENT_DIFFICULTIES)

	eventDifficulty = models.CharField(max_length=10, choices = LEVELS)

    
	#Template for the description about the trip.
	eventDescriptionTemplate = 'events/hike_description.html'

class DinnerEventModel(EventModel): # How do we implement this?
	eventType = 'Dinner'


class GenericTripModel(EventModel):
	eventType = 'Other Trip'
	eventDateEnd = models.DateTimeField(auto_now=False,auto_now_add=False, blank=True, null=True)
	#eventDuration = models.CharField(max_length=30, blank=True)
	#eventDestination = models.CharField(max_length=200, blank=True)
	#should this be TextField? How do we want to implement multidestinations?

	#Template for the description about the trip.
	eventDescriptionTemplate = 'events/generic_description.html'

class GenericGatheringModel(EventModel):
	eventType = 'Other Gathering'
	eventDateEnd = models.DateTimeField(auto_now=False,auto_now_add=False, blank=True, null=True)
	eventDescriptionTemplate = 'events/other_description.html'

