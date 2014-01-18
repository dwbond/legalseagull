from django.conf.urls import patterns, include, url

from courts.views import index

urlpatterns = patterns('',
    url(r'^$', index),
)
