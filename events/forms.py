from django import forms
from django.forms.extras.widgets import SelectDateWidget
import datetime
#from static import create_event.js
from models import EventModel, HikeEventModel, DinnerEventModel, GenericTripModel, GenericGatheringModel



class EventForm(forms.ModelForm):

	class Meta:
		model = EventModel
		fields = ('eventName', 'eventLocation', 'eventDateStart', 'eventDescription',)
		
		eventName = forms.CharField()
		eventDescription = forms.CharField()
		eventLocation = forms.CharField()
		eventDateStart = forms.DateField()
		widgets = {'eventName': forms.TextInput(attrs={'label':'Event Name'}) , 'eventLocation': forms.TextInput(attrs={'label':'Location'}), 'eventDateStart' : SelectDateWidget(attrs={"initial":"datetime.date.today()",}), 'eventDescription': forms.TextInput(attrs={'label':'Description','max_length':'500'}), }
		



class HikeForm(EventForm):
	picture = forms.ImageField()

	class Meta:
		model = HikeEventModel
		fields = ('eventDateEnd', 'eventDuration', 'eventElevation', 'eventDistance', 'eventDifficulty', 'picture',)
		eventDifficulty = forms.ChoiceField()
		eventElevation = forms.FloatField()
		eventDistance = forms.FloatField()
		eventDuration = forms.TextInput(attrs={'label':'Duration'})

		widgets = {'eventDateEnd' : SelectDateWidget(),  'eventDifficulty' : forms.Select(choices=HikeEventModel.LEVELS,)}


class DinnerForm(EventForm):
	picture = forms.ImageField()

	class Meta:
		model = DinnerEventModel
		fields = ( 'picture',)

class GenericTripForm(EventForm):
	picture = forms.ImageField()

	class Meta:
		model = GenericTripModel
		fields = ('eventDateEnd', 'picture',)
		widgets = {'eventDateEnd' : SelectDateWidget(), }

class GenericGatheringForm(EventForm):
	picture = forms.ImageField()

	class Meta:
		model = GenericGatheringModel
		fields = ('eventDateEnd', 'picture',)
		widgets = {'eventDateEnd' : SelectDateWidget(), }


