from django.db import models
from django.contrib.auth.models import User
from events.models import EventModel
from localflavor.us.us_states import US_STATES


class WeatherModel(models.Model):
	WEATHER_CHOICES = (('F', 'Fahrenheit'), ('C', 'Celsius'))
	event = models.ForeignKey(EventModel)
	degreeType = models.CharField(choices = WEATHER_CHOICES, max_length = 15, default='F')
	city = models.CharField(max_length=25, default = 'Ames')
	state = models.CharField(choices = US_STATES, max_length = 25, default = 'IA')
	
