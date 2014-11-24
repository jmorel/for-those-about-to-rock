from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from ftatr import views, settings, feeds

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ftatr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^feed/rocking-chairs-latest$', feeds.LatestRockingChairsFeed(), name='rocking-chair-feed'),
    url(r'^$', views.index, name='rocking-chair-index'),
    url(r'^rocking-chair/(?P<slug>\w+)$', views.show, name='rocking-chair-show'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
