import smtplib

from django import forms
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField(required = True)
	first_name = forms.CharField(max_length = 50, required = True)
	last_name = forms.CharField(max_length = 50, required = True)

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')

	def save(self, commit = True):
		user = super(UserRegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.set_password(self.cleaned_data['password1'])

		if commit == True:
			user.save()
		return user



		
