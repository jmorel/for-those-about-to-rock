from django.contrib.sitemaps import Sitemap
from anthology.models import RockingChair, Designer, Manufacturer


class RockingChairSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return RockingChair.objects.published().order_by('-published_at')

    def lastmod(self, obj):
        return obj.updated_at


class DesignerSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return Designer.objects.with_published_rocking_chairs()\
            .exclude(rocking_chairs=None) \
            .order_by('last_name')

    def lastmod(self, obj):
        return obj.updated_at


class ManufacturerSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return Manufacturer.objects.with_published_rocking_chairs() \
            .order_by('name')

    def lastmod(self, obj):
        return obj.updated_at
