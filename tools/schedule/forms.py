from django import forms
from models import ScheduleModel
from django.forms.extras.widgets import SelectDateWidget
import datetime

class ScheduleForm(forms.ModelForm):

	class Meta:
		model = ScheduleModel
		fields = ('name', 'description', 'start_date', 'end_date',)
		exclude = ('event',)
		widgets = {'start_date' : SelectDateWidget(), 'end_date' : SelectDateWidget(), }
		
