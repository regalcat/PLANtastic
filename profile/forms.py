from django import forms
from profile.models import Profile
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ('birthday', 'gender',)


class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email',)
