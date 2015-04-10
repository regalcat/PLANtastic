from django.conf.urls import patterns, url, include

from eventHomeView import eventHomeView
from invite.forms import InviteForm
from invite.views import InviteView
from events import views

urlpatterns = patterns('',
	url(r'^$', eventHomeView.as_view(), name='eventHome'),
	url(r'^invite', InviteView.as_view(), name='invite'),
	url(r'^invite-action', InviteForm, name='invite-action'),
	url(r'^tools/', include('tools.urls')),
	url(r'^editMembers', views.editMembers, name='editMembers'),

)
