from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from legalseagull.views import index
from legalseagull.forms import StyledSearchForm
from haystack.views import SearchView


urlpatterns = patterns('',
    # LegalSeagull default urls.
    url(r'^$', index),

    # App sub-urls.
    url(r'^legislation/', include('legislation.urls')),
    url(r'^courts/', include('courts.urls')),

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

    # Social-auth login urls.
    url(r'', include('social_auth.urls')),
)
