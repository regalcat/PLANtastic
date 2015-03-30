from django.conf.urls import patterns, url
## from django.core.urlresolvers import reverse
from register import views
from register.views import UserCreate 
from django.contrib.auth.views import login, logout
## urls.py

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'(?P<userID>\d+)/$', views.profile, name = 'profile'),
	url(r'^add/$', UserCreate.as_view(), name = 'create_user'),
	url(r'^register/$', views.register, name = 'register'),
	url(r'^login/$', login, {'template_name' : 'register/login.html'}, {'sucess_url' : '/'}),
	url(r'^logout/$', logout),
	url(r'^add/created/$', views.created, name = 'created'),


) 

 
