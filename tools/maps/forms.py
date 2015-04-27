from django import forms
from models import Gmap
from events.models import EventModel


class MapForm(forms.ModelForm):
	
	class Meta:
		model = Gmap
		fields = ('location',)
		exclude = ('event',)
		widgets = {'location' : forms.TextInput(attrs={'max_length':'100'}),}



