from django import forms
from django.forms.extras.widgets import SelectDateWidget
import datetime
from models import EventModel, HikeEventModel, DinnerEventModel, GenericTripModel, GenericGatheringModel

class EventForm(forms.ModelForm):

	class Meta:
		model = EventModel
		fields = ('eventName', 'eventLocation', 'eventDateStart', 'eventDescription', 'eventType',)
		eventType = forms.ChoiceField(choices=EventModel.EVENT_TYPES)
		eventName = forms.CharField()
		eventDescription = forms.CharField()
		eventLocation = forms.CharField()
		widgets = {'eventName': forms.TextInput(attrs={'label':'Event Name'}) , 'eventLocation': forms.TextInput(attrs={'label':'Location'}), 'eventDateStart' : SelectDateWidget(), 'eventDescription': forms.TextInput(attrs={'label':'Description','max_length': 500}), 'eventType' : forms.RadioSelect(choices=EventModel.EVENT_TYPES)}

class HikeForm(EventForm):

	class Meta:
		model = HikeEventModel
		fields = ('eventDateEnd', 'eventDuration', 'eventElevation', 'eventDistance', 'eventDifficulty',)
		eventDifficulty = forms.ChoiceField()
		eventDuration = forms.CharField()
		widgets = {'eventDateEnd' : SelectDateWidget(), 'eventElevation': forms.FloatField(), 'eventDistance': forms.FloatField() , 'eventDifficulty' : forms.Select(choices=HikeEventModel.LEVELS)}

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
		fields = ('eventName', 'eventLocation', 'eventDateStart', 'eventType',)
		eventType = forms.ChoiceField()
		widgets = {'eventName': forms.Textarea() , 'eventLocation': forms.Textarea(), 'eventDateStart' : SelectDateWidget(), 'eventType' : forms.RadioSelect(choices=EventModel.EVENT_TYPES,)}



