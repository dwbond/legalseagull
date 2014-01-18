from django.conf.urls import patterns, include, url

from courts.views import index, justice, tags, opinion, case

urlpatterns = patterns('',
    # homepage
    url(r'^$', index),
    
    # justice
    url(r'^justice/(?P<slug>([A-Za-z0-9\-\_]+))$', justice),

    # tags
    url(r'^tags/(?P<slug>([A-Za-z0-9\-\_]+))$', tags),

    # opinion
    url(r'^opinion/(?P<slug>([A-Za-z0-9\-\_]+))$', opinion),

    # case
    url(r'^case/(?P<slug>([A-Za-z0-9\-\_]+))$', case),
)
