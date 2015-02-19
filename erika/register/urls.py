from django.conf.urls import patterns, url
from register import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'(?P<userID>\d+)/$', views.profile, name = 'profile'),
	url(r'^register/$', views.register, name = 'register'),
) 

 
