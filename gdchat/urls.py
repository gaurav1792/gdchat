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
    url(r'^admin/', include(admin.site.urls)),
)
