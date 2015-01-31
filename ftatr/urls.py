from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
from haystack.views import SearchView
from ftatr import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ftatr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', RedirectView.as_view(url='/rocking-chair')),
    url(r'^rocking-chair/', include('rocking_chair.urls', namespace='rocking_chair')),
    url(r'^search/', SearchView(template='search/search.html.jinja2'), name='search'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
