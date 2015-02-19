from django.conf.urls import patterns, url
from base import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^base/$', views.base, name='base'),
)
