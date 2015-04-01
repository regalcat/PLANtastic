from django.conf.urls import patterns, url
from base import views
from base.invite.views import InviteView
from base.events.EventHomeView import EventHomeView
from base import forms

urlpatterns = patterns('',
	url(r'^(?P<eventid>\d+)/$', EventHomeView.as_view(), name='eventHome'),
	url(r'^(?P<eventid>\d+)/invite', InviteView.as_view(), name=('invite')),
	url(r'^(?P<eventid>\d+)/invite-action', forms.InviteForm, name=('invite-action')),

)
