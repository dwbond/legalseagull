from django.conf.urls import patterns, include, url

from legislation.views import index

urlpatterns = patterns('',
    url(r'^$', index),
)
