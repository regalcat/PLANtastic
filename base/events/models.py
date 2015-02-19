from django.db import models
#from base.models import UserModel

class EventModel(models.Model):
	eventid = models.ForeignKey(primary_key=True)
	event_name = models.CharField(max_length=50)
	event_location = models.CharField(max_length=50)
	event_location.blank = True
	event_date_start = models.DateTimeField(auto_now=False,auto_now_add=False)
	event_date_start.blank = True
	event_type = ('Dinner','Hike','Other Trip','Other Gathering')
	event_description = models.CharField(max_length=250)
	event_description.blank = True

class HikeEventModel(EventModel):
	event_type = 'Hike'
	event_date_end = models.DateTimeField(auto_now=False,auto_now_add=False)
	event_date_end.blank = True
	event_elevation = models.IntegerField()
	event_elevation.blank = True
	event_difficulty = ('Unknown','Easy','Moderate','Difficult','Strenuous','Technical')
	event_distance = models.FloatField()
        event_distance.blank = True
	event_duration = models.DateTimeField(auto_now=False,auto_now_add=False)
	event_duration.blank = True

class GenericTripModel(EventModel):
	event_type = 'Other Trip'
	event_date_end = models.DateTimeField(auto_now=False,auto_now_add=False)
	event_date_end.blank = True
	event_duration = models.DateTimeField(auto_now=False,auto_now_add=False)
	event_duration.blank = True
	event_destination = models.CharField(max_length=200)
	#should this be TextField? How do we want to implement multidestinations?

class GenericGatheringModel(EventModel):
	event_type = 'Other Gathering'
	event_date_end = models.DateTimeField(auto_now=False,auto_now_add=False)
	event_date_end.blank = True
	
	
	
        
        
        

