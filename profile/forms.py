from django import forms
from base.profile.models import Profile

class ProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ('birthday',)


