from django.conf.urls import patterns, url
from tools.schedule import views

urlpatterns = patterns('', 
	url(r'^$', views.showSchedule, name='scheduleIndex'),
	url(r'^editActivity/', views.editActivity, name='editActivity'),
	url(r'^addActivity/', views.addActivity, name='addActivity'),
	url(r'^deleteActivity/', views.deleteActivity, name='deleteActivity'),
)
