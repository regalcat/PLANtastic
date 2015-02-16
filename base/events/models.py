from django.db import models
from base.models import UserModel

class EventModel(models.Model):
	eventid = models.ForeignKey(primary_key=True)
	event_name = models.CharField(max_length=50)
	event_location = models.CharField(max_length=50)
	event_date_start = models.DateTimeField(auto_now=False,auto_now_add=False)
        event_type = ('Dinner','Hike','Other Trip','Other Gathering')

class HikeEventModel(models.Model) extends EventModel:
        event_type = 'Hike'
        event_date_end = models.DateTimeField(auto_now=False,auto_now_add=False)
        event_date_end.blank = True
        
        
        

