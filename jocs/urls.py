from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from main.views import *
from django.contrib.auth import logout
from django.shortcuts import redirect

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',mainpage),
    #url(r'^user/(\w+)/$', userpage),
    url(r'^login/$','django.contrib.auth.views.login'),

    #PLATFORMS
    url(r'^PC$',gamesByPlatform),
    url(r'^PlayStation 3$',gamesByPlatform),
    url(r'^Xbox 360$',gamesByPlatform),
    url(r'^Wii$',gamesByPlatform),
    url(r'^PSP$',gamesByPlatform),
    url(r'^Nintendo DS$',gamesByPlatform),
    url(r'^Mobile$',gamesByPlatform),
    
    #GAME INFO
    url(r'^PC/([\w\s]+)$',gameDetails),
    url(r'^PlayStation 3/([\w\s]+)$',gameDetails),
    url(r'^Xbox 360/([\w\s]+)$',gameDetails),
    url(r'^Wii/([\w\s]+)$',gameDetails),
    url(r'^PSP/([\w\s]+)$',gameDetails),
    url(r'^Nintendo DS/([\w\s]+)$',gameDetails),
    url(r'^Mobile/([\w\s]+)$',gameDetails),
    #url(r'^([\w\s]+)/([\w\s]+)$',gameDetails),
    #url(r'^jocs/', include('jocs.foo.urls')),

    #GAME BY 
    url(r'^company/([\w\s]+)$',gameByCompany),
    url(r'^type/([\w\s]+)$',gameByType),

    #COMMENT
    #url(r'^comment$/([\w\s]+)',Comment),
    url(r'^review/add/([\w\s]+)/([\w\s]+)$',AddReview),#Comentari
    url(r'^review/edit/([\w\s]+)/([\w\s]+)/([\w\s]+)$',EditReview),
    url(r'^review/delete/([\w\s]+)/([\w\s]+)/([\w\s]+)$',DeleteReview),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$',Logout),
    url(r'^register$',register))
