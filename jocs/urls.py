from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from main.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', mainpage, name='home'),
    url(r'^user/(\w+)/$', userpage),
    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^pc$','main.views.pc'),
    url(r'^ps3$','main.views.ps3'),
    url(r'^xbox360$','main.views.xbox360'),
    url(r'^wii$','main.views.wii'),
    url(r'^vita$','main.views.vita'),
    url(r'^n3ds$','main.views.n3ds'),
    url(r'^mobile$','main.views.mobile'),
    #Elems
    url(r'^pc$','main.views.pc'),
    url(r'^ps3$','main.views.ps3'),
    url(r'^xbox360$','main.views.xbox360'),
    url(r'^wii$','main.views.wii'),
    url(r'^vita$','main.views.vita'),
    url(r'^n3ds$','main.views.n3ds'),
    url(r'^mobile$','main.views.mobile'),

    #url(r'^jocs/', include('jocs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^logout/$','main.views.logout'))
