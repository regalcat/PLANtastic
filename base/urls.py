from django.conf.urls import patterns, url

from base import views
from base.invite.views import InviteView
from base.events.EventHomeView import EventHomeView
from base import forms

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^home/', views.home, name='home'),
	url(r'^(?P<eventid>\d+)/$', EventHomeView.as_view(), name='eventHome'),
	url(r'^upcoming/', views.upcoming, name='upcoming'),
	url(r'^past/', views.past, name='past'),
	url(r'^logout/', views.logout, name='logout'),
	url(r'^login/', views.login, name='login'),
	url(r'^loginRequired/', views.loginRequired, name='loginrequired'),
	url(r'^register/', views.register, name='register'),
	url(r'^auth/', views.authView, name='authView'),
	url(r'^invalid/', views.invalidLogin, name='invalidLogin'),
	url(r'^registerSuccess/', views.registerSuccess, name='registerSuccess'),
	url(r'^new', views.new, name='new_event'),
	url(r'^delete/', views.deleteEvent, name='deleteEvent'), 

 	#url(r'^new', event_views.new, name='new_event'),

	#Urls pertaining to email invites
	url(r'^(?P<eventid>\d+)/invite', InviteView.as_view(), name=('invite')),
	url(r'^(?P<eventid>\d+)/invite-action', forms.InviteForm, name=('invite-action')),
	url(r'^join', views.join_event, name=('join-event')),
	url(r'^cover-pic/', views.coverPic, name='cover-pic'),
)
