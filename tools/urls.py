from django.conf.urls import patterns, include, url

from tools.upload_pics import views

urlpatterns = patterns('',
	url(r'^item_share/', include('tools.item_share.urls')),
	url(r'^upload_pics/', views.UploadPicFormView.as_view(), name="upload-pics"),
)
