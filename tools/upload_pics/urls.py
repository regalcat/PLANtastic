from django.conf.urls import patterns, url
from .UploadPicView import UploadPicFormView
from .MainView import MainView
from .EditPicView import EditPicView

urlpatterns = patterns('',
	url(r'^$', MainView.as_view(), name='upload_pics.index'),
	url(r'^upload_pic/$', UploadPicFormView.as_view(), name='upload-pic'),
	url(r'^edit_pic/(?P<pk>\d+)$', EditPicView.as_view(), name='edit-pic'),
)
