from django import forms
from django.forms.extras.widgets import SelectDateWidget
import datetime

class EventForm(forms.ModelForm):

	class Meta:
		model = eventModel
		fields = ('eventName', 'eventLocation', 'eventDateStart', 'eventType',)
		widgets = {'eventName': forms.Textarea() , 'eventLocation': forms.Textarea(), 'eventDateStart' : SelectDateWidget(), 'eventType' : forms.ChoiceField(choices=EVENT_TYPES, widget=forms.RadioSelect()), }
		
