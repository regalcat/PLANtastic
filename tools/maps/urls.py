from django.conf.urls import patterns, url

from .MapView import MapView
from views import mapsEditView, mapsView, addMapView, deleteMapView, executeDeleteView



urlpatterns = patterns('', 
	url(r'^$', mapsView, name='maps'),
	url(r'^addMap/$', addMapView, name='addMap'),
	url(r'^editMap/(?P<mapid>\d+)/$', mapsEditView, name='editMap'),
	url(r'^deleteMap/(?P<mapid>\d+)/$', deleteMapView, name='deleteMap'),
	url(r'^executeDelete/(?P<mapid>\d+)/$', executeDeleteView, name='executeDelete'),
)
