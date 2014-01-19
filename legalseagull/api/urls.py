from django.conf.urls import patterns, include, url
from api.views import index, evernote_create_note, evernote_create_notebook

urlpatterns = patterns('',
    url(r'^$', index, name='api_index'),
    url(r'^evernote/create-note/$',
        evernote_create_note, name='create_note'),
    url(r'^evernote/create-notebook/$',
        evernote_create_notebook, name='create_notebook'),
)
