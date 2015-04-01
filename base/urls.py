from django.conf.urls import patterns, url

from base import views
from base.invite.views import InviteView
#from base.events.EventHomeView import EventHomeView
from base import forms
from events import EventHomeView
from events import forms
from profile import forms
from profile import views


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^home/', views.home, name='home'),
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
	
	#add event id to url	
	url(r'^delete/', views.deleteEvent, name='deleteEvent'), 


	#urls pertaining to profiles
	url(r'^$', views.profile, name='profile'),
	url(r'^manageAccount/$', profile.views.manageAccount, name='manageAccount'),
	url(r'^checkInformation/$', profile.views.checkInformation, name='checkInformation'),
	url(r'^editInformation/$', profile.views.editInformation, name='editInformation'),


	#Urls pertaining to email invites
	url(r'^join', views.join_event, name=('join-event')),
	url(r'^cover-pic/', views.coverPic, name='cover-pic'),
)
