from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'planner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('base.urls', namespace='base')),
	url(r'^(?P<eventid>\d+)/', include('events.urls', namespace='events')),
	url(r'^profile/', include('profile.urls', namespace='profile')),
	url(r'^notifications', include('notifications.urls', namespace='notifications')),
	url(r'^friends/', include('friends.urls', namespace='friends')),
)
