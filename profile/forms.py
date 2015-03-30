from django import forms
#from django.forms import widgets
from profile.models import Profile
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
import datetime
 

class ProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ('birthday', 'gender', 'description',)
		widgets = {'description': forms.Textarea() , 'birthday' : SelectDateWidget(years = range(datetime.date.today().year, 1930, -1)) }
		


class UserForm(forms.ModelForm):
	first_name = forms.CharField(max_length=30, required=True)
	last_name = forms.CharField(max_length=30, required=True)
	email = forms.EmailField(required=True)
	

	class Meta:
		model = User
		fields = {'first_name', 'last_name', 'email',}
		
		
