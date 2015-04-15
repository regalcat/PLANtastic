from django.conf.urls import patterns, url
from tools.allergy_list import views

urlpatterns = patterns('', 
	url(r'^$', views.allergyindex, name='allergyindex'),
	url(r'^addAllergy', views.addAllergy, name='addAllergy'),
)
