from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('', 
	url(r'^new/$', views.newEvent, name='newEvent'),
	#url(r'^invite/$', views.inviteFriends, name='inviteFriends'
)

