from django.conf.urls import patterns, url

from .MapView import MapView
from views import mapsEditView



urlpatterns = patterns('', 
	url(r'^$', mapsEditView, name='edit'),

)
