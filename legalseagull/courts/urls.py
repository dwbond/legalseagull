from django.conf.urls import patterns, include, url

from courts.views import index, justice, tags, opinion, case

urlpatterns = patterns('',
    # homepage
    url(r'^$', index),
    
    # justice
    url(r'^(?P<slug>\w+)/?$', justice),

    # tags
    url(r'^(?P<slug>\w+)/?$', tags),

    # opinion
    url(r'^(?P<slug>\w+)/?$', opinion),

    # case
    url(r'^(?P<slug>\w+)/?$', case),
)
