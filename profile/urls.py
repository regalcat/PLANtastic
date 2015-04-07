from django.conf.urls import patterns, url
from profile import views

urlpatterns = patterns('',
	url(r'^$', views.profile, name='profile'),
	url(r'^manageAccount/$', views.manageAccount, name='manageAccount'),
	url(r'^checkInformation/$', views.checkInformation, name='checkInformation'),
	url(r'^editInformation/$', views.editInformation, name='editInformation'),
	url(r'^deleteAccount/$', views.deleteAccount, name='deleteAccount'),
	url(r'^executeDelete/$', views.executeDelete, name='executeDelete'),


)
