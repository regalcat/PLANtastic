from django import forms
from django.contrib.auth.models import User
from models import FriendList
from events.models import EventModel


class AddFriendForm(forms.ModelForm):
	
	class Meta:
		model = FriendList
		fields = ('friends',)
		widgets = {'friends' : forms.TextInput(attrs={'max_length':'30', 'label':'Username'})}


