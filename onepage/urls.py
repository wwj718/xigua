#coding=utf-8


from django.conf.urls import patterns, url

from django.views.generic.simple import direct_to_template


urlpatterns = patterns("",
    (r'^aboutus/$', direct_to_template, {'template': 'aboutus.html'}),

)
