from django import forms
from django.forms.extras.widgets import SelectDateWidget
import datetime
#from static import create_event.js
from models import EventModel, HikeEventModel, DinnerEventModel, GenericTripModel, GenericGatheringModel


class EventTypeForm(forms.ModelForm):
	class Meta:
		model = EventModel
		fields = ('eventType',)
		eventType = forms.ChoiceField()
		widgets={'eventType' : forms.RadioSelect(attrs={'choices':'EventModel.EVENT_TYPES', 'onchange':'event();'})}
		


class EventForm(forms.ModelForm):

	class Meta:
		model = EventModel
		fields = ('eventName', 'eventLocation', 'eventDateStart', 'eventDescription',)
		
		eventName = forms.CharField()
		eventDescription = forms.CharField()
		eventLocation = forms.CharField()
		widgets = {'eventName': forms.TextInput(attrs={'label':'Event Name'}) , 'eventLocation': forms.TextInput(attrs={'label':'Location'}), 'eventDateStart' : SelectDateWidget(), 'eventDescription': forms.TextInput(attrs={'label':'Description','max_length':'500'}), }
		
class HikeForm(EventForm):

	class Meta:
		model = HikeEventModel
		fields = ('eventDateEnd', 'eventDuration', 'eventElevation', 'eventDistance', 'eventDifficulty',)
		eventDifficulty = forms.ChoiceField()
		widgets = {'eventDateEnd' : SelectDateWidget(), 'eventDuration': forms.TextInput(attrs={'label':'Duration'}) , 'eventElevation': forms.FloatField(), 'eventDistance': forms.FloatField() , 'eventDifficulty' : forms.Select(choices=HikeEventModel.LEVELS,)}

class DinnerForm(EventForm):

	class Meta:
		model = DinnerEventModel
		

class GenericTripForm(EventForm):

	class Meta:
		model = GenericTripModel
		fields = ('eventDateEnd',)
		widgets = {'eventDateEnd' : SelectDateWidget(), }

class GenericGatheringForm(EventForm):

	class Meta:
		model = GenericGatheringModel
		fields = ('eventDateEnd',)
		widgets = {'eventDateEnd' : SelectDateWidget(), }
