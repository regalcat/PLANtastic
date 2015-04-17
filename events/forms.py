from django import forms
from django.forms.extras.widgets import SelectDateWidget
import datetime
#from static import create_event.js
from models import EventModel, HikeEventModel, DinnerEventModel, GenericTripModel, GenericGatheringModel



class EventForm(forms.ModelForm):

	class Meta:
		model = EventModel
		fields = ('name', 'location', 'event_Start_Date', 'event_Description',)
		exclude = ('eventType',)
		
		name = forms.CharField()
		event_Description = forms.CharField()
		location = forms.CharField()
		event_Start_Date = forms.DateField()
		widgets = {'name': forms.TextInput() , 'location': forms.TextInput(attrs={'label':'location'}), 'event_Start_Date' : SelectDateWidget(attrs={"initial":"datetime.date.today()","label": "Event Start Date"}), 'event_Description': forms.TextInput(attrs={'label':'Event Description','max_length':'500'}), }
		



class HikeForm(EventForm):

	class Meta:
		model = HikeEventModel
		fields = ('event_End_Date', 'duration', 'elevation', 'distance', 'difficulty',)
		exclude = ('eventType',)
		eventDifficulty = forms.ChoiceField()
		eventElevation = forms.FloatField()
		eventDistance = forms.FloatField()
		eventDuration = forms.TextInput(attrs={'label':'Duration'})

		widgets = {'event_End_Date' : SelectDateWidget(),  'difficulty' : forms.Select(choices=HikeEventModel.LEVELS,)}


class DinnerForm(EventForm):

	class Meta:
		model = DinnerEventModel
		exclude = ('eventType',)

class GenericTripForm(EventForm):

	class Meta:
		model = GenericTripModel
		fields = ('event_End_Date',)
		exclude = ('eventType',)
		widgets = {'event_End_Date' : SelectDateWidget(), }

class GenericGatheringForm(EventForm):

	class Meta:
		model = GenericGatheringModel
		fields = ('event_End_Date',)
		exclude = ('eventType',)
		widgets = {'event_End_Date' : SelectDateWidget(), }


