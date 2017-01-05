from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic import RedirectView
from haystack.views import SearchView
from ftatr import settings, views
from anthology.sitemaps import RockingChairSitemap, DesignerSitemap, ManufacturerSitemap, StaticSitemap

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/rocking-chair')),
    url(r'^about/?', views.about, name='about'),
    url(r'^contact/?', views.contact, name='contact'),
    url(r'^rocking-chair/', include('anthology.urls.rocking_chair', namespace='rocking_chair')),
    url(r'^manufacturer/', include('anthology.urls.manufacturer', namespace='manufacturer')),
    url(r'^designer/', include('anthology.urls.designer', namespace='designer')),
    url(r'^analytics/', include('anthology.urls.analytics', namespace='analytics')),
    url(r'^contribution/', include('anthology.urls.contribution', namespace='analytics')),
    url(r'^search/', SearchView(template='search/search.html.jinja2'), name='search'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'rocking_chair': RockingChairSitemap,
                                                  'designer': DesignerSitemap,
                                                  'manufacturer': ManufacturerSitemap,
                                                  'static': StaticSitemap}},
         name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
