from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from . import views, settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ftatr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^rocking-chair/(?P<slug>\w+)$', views.show, name='show'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
