
#python libraries
import smtplib
#django libraries
from django import forms
from django.core.mail import send_mail

class InviteForm(forms.Form):
	email = forms.EmailField(required=True)
	
	#A rather long function that sends the email. Takes in the InviteForm object that called it.
	def send_email(self):
		gmail_user = 'mail.plantastic@gmail.com'
		gmail_passwd = 'QwertyQwerty123' #This seems like a horrible idea. I'll find a better way later.
		smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
		smtpserver.ehlo()
		smtpserver.starttls()
		smtpserver.login(gmail_user, gmail_passwd)
		header = 'To:' + self.email +'\n' + gmail_user + '\n' + 'Subject: Plantastic Test Invite \n'
		print header
		msg = header + '\n This is a test email \n\n'
		smtpserver.sendmail(gmail_user, to, msg)
		print 'Email sent!'
		smtpserver.close()
		#Uncomment to use the Django send_mail function. (Doesn't work right now)
		#send_mail('Invitation to join a PLANtastic event!', 
		#	, 'plantastic@gmail.com', [email], html_message=invitemsg.html)
		
