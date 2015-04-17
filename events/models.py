from django.db import models

class EventModel(models.Model):
	eventid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	location.blank = True
	event_Start_Date = models.DateField(auto_now=False,auto_now_add=False)
	
	EVENT_TYPES = (
		('dinner', 'Dinner'), 
		('hike', 'Hike'), 
		('otherTrip', 'Other Trip'),
		('otherGathering', 'Other Gathering'),
	)

	
	eventType = models.CharField(max_length=20, choices=EVENT_TYPES, blank=False, default=None)
	event_Description = models.CharField(max_length=500)
	event_Description.blank = True
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
		if (events.count() == 1):
			return events[0]
		events = GenericGatheringModel.objects.filter(eventid=event_id)
		if events.count() == 1:
			return events[0]
		events = DinnerEventModel.objects.filter(eventid=event_id)
		if (events.count() == 1):
			return events[0]
		return EventModel.objects.get(eventid=event_id)

	def createEvent(self,name,location,event_Start_Date,eventType,event_Description):
		self.name=name
		self.location=location
		self.event_Start_Date=event_Start_Date
		self.eventType=eventType
		self.event_Description=event_Description
		self.save()
		return self

	@staticmethod
	def getEventTypes():
		return ('Dinner', 'Hike', 'Other Trip', 'Other Gathering')

class HikeEventModel(EventModel):
	LEVELS = (('unknown', 'Unknown'), ('easy', 'Easy'), ('moderate', 'Moderate'), ('difficult', 'Difficult'),
	('strenuous', 'Strenuous'), ('technical', 'Technical'),)
	
	eventType = 'Hike'
	event_End_Date = models.DateField(auto_now=False,auto_now_add=False, blank=True, null=True)
	duration = models.CharField(max_length=30, blank=True)
	elevation = models.IntegerField(blank=True, null=True)
	distance = models.FloatField(blank=True, null=True)

	#EVENT_DIFFICULTIES= (
	#	('unknown', 'Unknown'),
	#	('easy', 'Easy'),
	#	('moderate', 'Moderate'),
	#	('difficult', 'Difficult'),
	#	('strenuous', 'Strenuous'),
	#	('technical', 'Technical'),
	#)
	#eventDifficulty = models.CharField(max_length=9, choices=EVENT_DIFFICULTIES)

	difficulty = models.CharField(max_length=10, choices = LEVELS)

    
	#Template for the description about the trip.
	eventDescriptionTemplate = 'events/hike_description.html'

class DinnerEventModel(EventModel): # How do we implement this?
	eventType = 'Dinner'


class GenericTripModel(EventModel):
	eventType = 'Other Trip'
	event_End_Date = models.DateField(auto_now=False,auto_now_add=False, blank=True, null=True)
	#eventDuration = models.CharField(max_length=30, blank=True)
	#eventDestination = models.CharField(max_length=200, blank=True)
	#should this be TextField? How do we want to implement multidestinations?

	#Template for the description about the trip.
	eventDescriptionTemplate = 'events/generic_description.html'

class GenericGatheringModel(EventModel):
	eventType = 'Other Gathering'
	event_End_Date = models.DateField(auto_now=False,auto_now_add=False, blank=True, null=True)
	eventDescriptionTemplate = 'events/other_description.html'

