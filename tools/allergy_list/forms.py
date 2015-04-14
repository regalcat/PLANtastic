from django import forms
from django.contrib.auth.models import User
from models import AllergyModel


class AllergyForm(forms.ModelForm):
	
	class Meta:
		model = AllergyModel
		fields = ('vegetarian', 'vegan', 'lactose', 'gluten', 'nuts', 'other',)
		exclude = ('user', 'event',)
		widgets = {'vegetarian': forms.CheckboxInput(), 'vegan': forms.CheckboxInput(), \
		'lactose': forms.CheckboxInput(), 'gluten': forms.CheckboxInput(), 'nuts': forms.CheckboxInput(),}
		
