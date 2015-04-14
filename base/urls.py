from django.conf.urls import patterns, url

from base import views as base_views
from events import views as event_views 
from invite import views as invite_views
from profile import views as profile_views
from users import views as users_views
from events import newEventView as new_event_views


urlpatterns = patterns('',
	url(r'^$', base_views.index, name='index'),
	url(r'^home/', base_views.home, name='home'),
	url(r'^cover-pic/', base_views.coverPic, name='cover-pic'),

	url(r'^upcoming/', event_views.upcoming, name='upcoming'),
	url(r'^past/', event_views.past, name='past'),
	url(r'^new', new_event_views.new, name='new_event'),

	url(r'^logout/', users_views.logout, name='logout'),
	url(r'^login/', users_views.login, name='login'),
	url(r'^loginRequired/', users_views.loginRequired, name='loginrequired'),
	url(r'^register/', users_views.register, name='register'),
	url(r'^auth/', users_views.authView, name='authView'),
	url(r'^invalid/', users_views.invalidLogin, name='invalidLogin'),
	url(r'^registerSuccess/', users_views.registerSuccess, name='registerSuccess'),
	
	#Urls pertaining to email invites
	url(r'^join', invite_views.join_event, name=('join-event')),
)
