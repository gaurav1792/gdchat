__author__ = 'gd'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gdchat.views.home', name='home'),
    url(r'^send_message', 'chat.views.send_message'),
    url(r'^get/(?P<u_id>\d+)/$', 'chat.views.user'),
    url(r'^get/(?P<u_id>\d+)/upload/$', 'chat.views.upload_image'),
    url(r'^get/(?P<u_id>\d+)/test11/$', 'chat.views.test11'),
    url(r'^mail/(?P<u_id>\d+)/$', 'chat.views.mailuser'),

)
