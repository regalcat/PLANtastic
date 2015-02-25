from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

#    url(r'^$', views.index, name = 'index'), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', include('register.urls')),
)



