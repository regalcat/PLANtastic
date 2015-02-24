
#python libraries
import smtplib
#django libraries
from django import forms
from django.core.mail import send_mail

class InviteForm(forms.Form):
	email = forms.EmailField(required=True)
	
	def send_email(self):
		send_mail('Invitation to join a PLANtastic event!', 
			, 'plantastic@gmail.com', [email], html_message=invitemsg.html)
		to
