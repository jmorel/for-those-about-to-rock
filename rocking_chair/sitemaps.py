import datetime
from django.contrib.sitemaps import Sitemap
from rocking_chair.models import RockingChair, Designer, Manufacturer


class RockingChairSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return RockingChair.objects \
            .exclude(published_at__gte=datetime.datetime.now()) \
            .exclude(published_at=None) \
            .order_by('-published_at')

    def lastmod(self, obj):
        return obj.updated_at


class DesignerSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return Designer.objects \
            .exclude(rocking_chairs=None) \
            .order_by('last_name')

    def lastmod(self, obj):
        return obj.updated_at


class ManufacturerSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return Manufacturer.objects \
            .exclude(rocking_chairs=None) \
            .order_by('name')

    def lastmod(self, obj):
        return obj.updated_at
