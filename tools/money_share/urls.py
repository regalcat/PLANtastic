from django.conf.urls import patterns, url

from .AddItemView import AddItemView
from .EditItemView import EditItemView
from .EditPaymentView import EditPaymentView
from .EditSettings import EditSettingsView
from .MainView import MainView
from .RecordPaymentView import RecordPaymentView

urlpatterns = patterns('', 
	url(r'^$', MainView.as_view(), name='money_share.index'),
	url(r'^add_item/$', AddItemView.as_view(), name='money_share.add-item'),
	url(r'^edit_item/(?P<pk>\d+)$', EditItemView.as_view(), name='edit-item'),
	url(r'^edit_payment/(?P<pk>\d+)$', EditPaymentView.as_view(), name='edit-payment'),
	url(r'^edit_settings/(?P<pk>\d+)$', EditSettingsView.as_view(), name='edit-settings'),
	url(r'^record_payment/$', RecordPaymentView.as_view(), name='record-payment'),
)
