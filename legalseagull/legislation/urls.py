from django.conf.urls import patterns, include, url
from legislation.views import index, view_title

urlpatterns = patterns('',
    url(r'^$', index, name='legislation_index'),
    url(r'^(?P<number>\d+)', view_title),
)
