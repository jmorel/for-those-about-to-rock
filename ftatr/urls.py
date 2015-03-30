from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic import RedirectView
from haystack.views import SearchView
from ftatr import settings
from rocking_chair.sitemaps import RockingChairSitemap, DesignerSitemap, ManufacturerSitemap

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/rocking-chair')),
    url(r'^rocking-chair/', include('rocking_chair.urls.rocking_chair', namespace='rocking_chair')),
    url(r'^manufacturer/', include('rocking_chair.urls.manufacturer', namespace='manufacturer')),
    url(r'^designer/', include('rocking_chair.urls.designer', namespace='designer')),
    url(r'^analytics/', include('rocking_chair.urls.analytics', namespace='analytics')),
    url(r'^search/', SearchView(template='search/search.html.jinja2'), name='search'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'rocking_chair': RockingChairSitemap,
                                                  'designer': DesignerSitemap,
                                                  'manufacturer': ManufacturerSitemap}},
         name='django.contrib.sitemaps.views.sitemap')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
