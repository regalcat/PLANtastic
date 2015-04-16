from django import forms
from localflavor.us import *
from localflavor.us.us_states import US_STATES

from models import WeatherModel


class WeatherForm(forms.ModelForm):
	
	class Meta:
		model = WeatherModel
		fields = ('degreeType', 'state', 'city',)
		exclude = ('event',)

		#widgets = {'state':forms.Select(choices = US_STATES)}

