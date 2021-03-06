from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gdchat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'chat.views.index'),
    url(r'^users/', include('chat.urls')),
    url(r'^login$', 'chat.views.login_view'),
    url(r'^logout$', 'chat.views.logout_view'),
    url(r'^signup$', 'chat.views.signup'),
    url(r'^chat$', 'chat.views.chat'),
    url(r'^test$', 'chat.views.test'),
    url(r'^test12$', 'chat.views.test12'),
    url(r'^test11$', 'chat.views.test11'),
    url(r'^chkstatus$', 'chat.views.chkstatus'),
    url(r'^send_message$', 'chat.views.send_message'),
    url(r'^set_online$', 'chat.views.set_online'),
    url(r'^test13$', 'chat.views.test13'),
    url(r'^setcounter$', 'chat.views.setcounter'),
    url(r'^create_post$', 'chat.views.create_post'),
    url(r'^admin/', include(admin.site.urls)),
)
