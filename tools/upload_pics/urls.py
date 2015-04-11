from django.conf.urls import patterns, url
from .UploadPicView import UploadPicFormView
from .MainView import MainView

urlpatterns = patterns('',
	url(r'^$', MainView.as_view(), name='upload_pics.index'),
	url(r'^upload_pic/$', UploadPicFormView.as_view(), name='upload-pic'),
)
