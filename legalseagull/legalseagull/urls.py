from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login, logout
from legalseagull.views import index, about, pricing, contact, terms, privacy
from legalseagull.forms import StyledSearchForm
from haystack.views import SearchView


urlpatterns = patterns('',
    # LegalSeagull default urls.
    url(r'^$', index),
    url(r'^about/$', about),
    url(r'^pricing/$', pricing),
    url(r'^contact/$', contact),
    url(r'^terms/$', terms),
    url(r'^privacy/$', privacy),

    # App sub-urls.
    url(r'^legislation/', include('legislation.urls')),
    url(r'^courts/', include('courts.urls')),
    url(r'^api/', include('api.urls')),

    # Admin interface.
    url(r'^admin/', include(admin.site.urls)),

    # Search urls.
    url(
        r'^search/?',
        SearchView(
            form_class = StyledSearchForm,
            results_per_page = 20,
        ),
        name = 'haystack_search',
    ),

    # Auth login urls.
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
)
