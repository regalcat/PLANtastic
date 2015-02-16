from django.conf.urls import patterns, url
from tools.item_share import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^form/$', views.form, name='form'),
)
