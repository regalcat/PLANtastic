from django.conf.urls import patterns, url
from profile import views

urlpatterns = patterns('',
	url(r'^$', views.profile, name='profile'),
	url(r'^manageAccount/$', views.manageAccount, name='manageAccount'),
	url(r'^checkInformation/$', views.checkInformation, name='checkInformation'),


)
