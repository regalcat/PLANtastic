from django.conf.urls import patterns, url

from .AddItemView import AddItemView
from .EditItemView import EditItemView
from .MainView import MainView
from .RecordPaymentView import RecordPaymentView

urlpatterns = patterns('', 
	url(r'^$', MainView.as_view(), name='money_share.index'),
	url(r'^add_item/$', AddItemView.as_view(), name='money_share.add-item'),
	url(r'^edit_item/(?<pk>\d+)$', EditItemView.as_view(), name='edit-item'),
	url(r'^record_payment/$', RecordPaymentView.as_view(), name='record-payment'),
)
