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
	url(r'^login/$', views.login, name='login'),
	url(r'^register/$', views.register, name='register'),
	url(r'^auth/$', views.authView, name='authView'),
	url(r'^invalid/$', views.invalidLogin, name='invalidLogin'),
	url(r'^registerSuccess/$', views.registerSuccess, name='registerSuccess'),
	url(r'^new',views.new, name='new_event')

	
)
