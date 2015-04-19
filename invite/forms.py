import smtplib

from django import forms
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from invite.models import MembershipModel

class InviteForm(forms.Form):
	email = forms.EmailField(required=True)
	
	#A rather long function that sends the email. Takes in the InviteForm object that called it.
	#Remember to go to gmail and allow access for less secure apps. (Wow. That sounds shady and janky.)
	@staticmethod
	def send_email(to, event, rstring):
		gmail_user = 'mail.plantastic@gmail.com'
		gmail_passwd = 'QwertyQwerty123' #This seems like a horrible idea. I'll find a better way later.
		smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
		smtpserver.ehlo()
		smtpserver.starttls()
		smtpserver.login(gmail_user, gmail_passwd)
		header = 'To:' + to +'\n' + gmail_user + '\n' + 'Subject: Plantastic Test Invite \n'
		#print header
		ename = event.name
		msg = header + '\n You have been invited to ' + ename + '! \n Your confirmation string is: '+ rstring +'\n Go to Plantastic and enter this string to join the event!\n\n'
		smtpserver.sendmail(gmail_user, to, msg)
		#print 'Email sent!'
		smtpserver.close()
		#Uncomment to use the Django send_mail function. (Doesn't work right now)
		#send_mail('Invitation to join a PLANtastic event!', msg, 'mail.plantastic@gmail.com', [to], fail_silently=False)


