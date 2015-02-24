from django.conf.urls import patterns, include, url
from django.contrib import admin
from base.invite.views import test

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'planner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', test),
    url(r'^(?P<eventid>\d+)/invite$', views.invite),
    url(r'^(?P<eventid>\d+)/invite-form$', views.InviteForm)
)

