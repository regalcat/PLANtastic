from django import forms
from django.contrib.auth.models import User
from models import Car, Person
from events.models import EventModel


class CarForm(forms.ModelForm):
	
	class Meta:
		model = Car
		fields = ('seats',)
		exclude = ('user', 'event',)
		widgets = {'seats' : forms.IntegerField(min_value = '0')}


class PersonForm(forms.ModelForm):
	
	class Meta:
		model = Person
		fields = ('personid', 'address')
		#cars = Car.cars.filter(event = self.event)
		#car = forms.ChoiceField()
		#personid = user
		widgets = {'address': forms.TextInput(attrs={'max_length':'50'}),}


