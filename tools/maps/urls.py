from django.conf.urls import patterns, url

from .MapView import MapView
from views import mapsEditView, mapsView, addMapView



urlpatterns = patterns('', 
	url(r'^$', mapsView, name='maps'),
	url(r'^addMap/$', addMapView, name='addMap'),
	url(r'^editMap/(?P<mapid>\d+)/$', mapsEditView, name='editMap'),

)
