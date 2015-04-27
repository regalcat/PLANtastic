from django.conf.urls import patterns, url
from profile import views
from settings import settings


urlpatterns = patterns('',
	url(r'^$', views.profile, name='profile'),
	url(r'^manageAccount/$', views.manageAccount, name='manageAccount'),
	url(r'^checkInformation/$', views.checkInformation, name='checkInformation'),
	url(r'^editInformation/$', views.editInformation, name='editInformation'),
	url(r'^deleteAccount/$', views.deleteAccount, name='deleteAccount'),
	url(r'^executeDelete/$', views.executeDelete, name='executeDelete'),
	url(r'^other/$', views.otherProfile, name ='otherProfile'),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),


)
