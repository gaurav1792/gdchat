__author__ = 'gd'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gdchat.views.home', name='home'),
    url(r'^send_message', 'chat.views.send_message'),
    url(r'^get/(?P<u_id>\d+)/$', 'chat.views.user'),
    url(r'^mail/(?P<u_id>\d+)/$', 'chat.views.mailuser'),

)
