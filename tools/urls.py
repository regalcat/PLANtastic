from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^allergy_list/', include('tools.allergy_list.urls', namespace = 'allergylist')),
	url(r'^item_share/', include('tools.item_share.urls', namespace = 'item_share')),
	url(r'^money_share/', include('tools.money_share.urls', namespace = 'money_share')),
	url(r'^upload_pics/', include('tools.upload_pics.urls')),
	url(r'^weather/', include('tools.weather.urls', namespace = 'weather')),
)
