from django.conf.urls import patterns, url
from tools.item_share.AddItemView import AddItemView
from tools.item_share.ItemShareView import ItemShareView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('', 
	url(r'^$', csrf_exempt(ItemShareView.as_view()), name='item_share.index'),
	url(r'^add_item/$', AddItemView.as_view(), name='add-item')
)
