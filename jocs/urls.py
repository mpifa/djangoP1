from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from main.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',mainpage),
    url(r'^user/(\w+)/$', userpage),
    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^pc$',pc),
    url(r'^ps3$',ps3),
    url(r'^xbox360$',xbox360),
    url(r'^wii$',wii),
    url(r'^vita$',vita),
    url(r'^n3ds$',n3ds),
    url(r'^mobile$',mobile),
    #Elems
    url(r'^pc/([\w\s]+)$',gameDetails),
    url(r'^ps3/([\w\s]+)$',gameDetails),
    url(r'^xbox360/([\w\s]+)$',gameDetails),
    url(r'^wii/([\w\s]+)$',gameDetails),
    url(r'^vita/([\w\s]+)$',gameDetails),
    url(r'^n3ds/([\w\s]+)$',gameDetails),
    url(r'^mobile/([\w\s]+)$',gameDetails),
    #url(r'^jocs/', include('jocs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^logout/$','django.contrib.auth.views.logout'))
