from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'for_those_about_to_rock.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index')
)
