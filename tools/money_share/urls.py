from django.conf.urls import patterns, url

from .AddItemView import AddItemView
from .MainView import MainView

urlpatterns = patterns('', 
	url(r'^$', MainView.as_view(), name='money_share.index'),
	url(r'^add_item/$', AddItemView.as_view(), name='money_share.add-item')
)
