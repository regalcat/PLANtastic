from django import forms
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import MsPaymentModel

class RecordPaymentForm(forms.ModelForm):

	class Meta:
		template_name='money_share/record_payment_form.html'
		model = MsPaymentModel
		fields = ('payer', 'receiver', 'amount')
		
		widgets = {'reciever': forms.Select(attrs={'choices':
