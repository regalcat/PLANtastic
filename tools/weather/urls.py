from django.conf.urls import patterns, url
from tools.weather import views

urlpatterns = patterns('', 
	url(r'^$', views.showWeather, name='showWeather'),
	url(r'^editWeather', views.editWeather, name='editWeather'),
)
