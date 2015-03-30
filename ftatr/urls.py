from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic import RedirectView
from haystack.views import SearchView
from ftatr import settings
from ftatr.sitemaps import FTATRSitemap

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/rocking-chair')),
    url(r'^rocking-chair/', include('rocking_chair.urls', namespace='rocking_chair')),
    url(r'^manufacturer/', include('manufacturer.urls', namespace='manufacturer')),
    url(r'^designer/', include('designer.urls', namespace='designer')),
    url(r'^analytics/', include('analytics.urls', namespace='analytics')),
    url(r'^designer/', include('designer.urls', namespace='designer')),
    url(r'^search/', SearchView(template='search/search.html.jinja2'), name='search'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'ftatr': FTATRSitemap}},
         name='django.contrib.sitemaps.views.sitemap')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
