from django.conf.urls import patterns, include, url
from django.contrib import admin
from base import urls as base_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'planner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^', include(base_urls))
)
