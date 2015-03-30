from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^item_share/', include('tools.item_share.urls')),
)
