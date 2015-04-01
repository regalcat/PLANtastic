from django.conf.urls import patterns, url

from base import views as base_views
from events import views as event_views 
from invite import views as invite_views
from profile import views as profile_views


urlpatterns = patterns('',
	url(r'^$', base_views.index, name='index'),
	url(r'^home/', base_views.home, name='home'),
	url(r'^cover-pic/', base_views.coverPic, name='cover-pic'),

	url(r'^upcoming/', event_views.upcoming, name='upcoming'),
	url(r'^past/', event_views.past, name='past'),
	url(r'^new', event_views.new, name='new_event'),
	#add event id to url	
	url(r'^delete/', event_views.deleteEvent, name='deleteEvent'), 

	url(r'^logout/', user_views.logout, name='logout'),
	url(r'^login/', user_views.login, name='login'),
	url(r'^loginRequired/', user_views.loginRequired, name='loginrequired'),
	url(r'^register/', user_views.register, name='register'),
	url(r'^auth/', user_views.authView, name='authView'),
	url(r'^invalid/', user_views.invalidLogin, name='invalidLogin'),
	url(r'^registerSuccess/', user_views.registerSuccess, name='registerSuccess'),
	
	#Urls pertaining to email invites
	url(r'^join', invite_views.join_event, name=('join-event')),
)
