from django.conf.urls import patterns, url, include

from eventHomeView import eventHomeView
from invite.forms import InviteForm
from invite.views import InviteView, usernameInvite
from events import views
from invite import views as invite_views

urlpatterns = patterns('',
	url(r'^$', eventHomeView.as_view(), name='eventHome'),
	url(r'^deleteEvent', views.deleteEvent, name='deleteEvent'),
	url(r'^executeDelete', views.executeDeleteEvent, name='executeDeleteEvent'),
	url(r'^invite', InviteView.as_view(), name='invite'),
	url(r'^invite-action', InviteForm, name='invite-action'),
	url(r'^username-invite', usernameInvite, name='invite-username'),
	url(r'^tools/', include('tools.urls', namespace='tools')),
	url(r'^editMembers', views.editMembers, name='editMembers'),
	url(r'^editEvent', views.editEvent, name='editEvent'),
	url(r'^deleteMember', views.deleteMember, name='deleteMember'),
	url(r'^executeMember', views.executeDeleteMember, name='executeDeleteMember'),
	url(r'^leaveEvent', views.leaveEvent, name='leaveEvent'),
	url(r'^executeLeaveEvent', views.executeLeaveEvent, name='executeLeaveEvent'),

)
