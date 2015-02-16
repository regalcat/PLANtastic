from django.conf.urls import patterns, url
from tools.item_share import views
from tools.item_share.AddItemView import AddItemView

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^form/$', views.form, name='form'),
	url(r'^add_item/$', AddItemView.as_view(), name='add-item')
)
