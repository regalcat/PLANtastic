from django.conf.urls import patterns, url
from base import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^home/$', views.home, name='home'),
	url(r'^(?P<eventid>\d+)/$', views.event_home),
	url(r'^upcoming/$', views.upcoming, name='upcoming'),
	url(r'^past/$', views.past, name='past'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^manage_account/$', views.manage_account, name='manage_acount'),
	url(r'^logout/$', views.logout, name='logout'),
# TODO 	url(r'^new', new_event_views.get_ name='new_event'
# TODO Login Url
# TODO REgister URL
	
)
