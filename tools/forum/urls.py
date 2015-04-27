from django.conf.urls import patterns, url
from tools.forum.views import ForumView, ThreadView

urlpatterns = patterns('',
	url(r'^$', ForumView.as_view(), name='forum'),
	url(r'^create-thread/$', ForumView.post, name='create-thread'),
	url(r'^(?P<threadid>\d+)/$', ThreadView.as_view(), name='thread'),
	url(r'^(?P<threadid>\d+)/reply-thread/$', ThreadView.post, name='reply-thread'),
)
