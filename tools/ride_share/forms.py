from django import forms
from django.contrib.auth.models import User
from models import Car, Person
from events.models import EventModel


class CarForm(forms.ModelForm):
	
	class Meta:
		model = Car
		fields = ('seats',)
		exclude = ('user', 'event',)
		widgets = {'seats' : forms.NumberInput()}


class PersonForm(forms.ModelForm):
	
	class Meta:
		model = Person
		fields = ('address',)
		widgets = {'address': forms.TextInput(attrs={'max_length':'50'}),}


