from django.conf.urls import patterns, url
from tools.weather import views

urlpatterns = patterns('', 
	url(r'^editWeather', views.editWeather, name='editWeather'),
)
