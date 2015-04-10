from django.conf.urls import patterns, url
from .AddItemView import AddItemView
from .ItemShareView import ItemShareView

#TODO (Susan): remove need for CSRF exemption for Ajax requests
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('', 
	url(r'^$', csrf_exempt(ItemShareView.as_view()), name='item_share.index'),
	url(r'^add_item/$', AddItemView.as_view(), name='add-item')
)
