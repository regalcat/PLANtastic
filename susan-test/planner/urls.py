from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import hello

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'planner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^hello/$', hello), 
)
