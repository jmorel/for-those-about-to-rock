import datetime
from django.db.models import Manager


class RockingChairManager(Manager):
    def published(self):
        rocking_chairs = self.filter(published_at__lte=datetime.datetime.now())
        return rocking_chairs


class DesignerManager(Manager):
    def with_published_rocking_chairs(self):
        designers = self \
            .filter(rocking_chairs__published_at__lte=datetime.datetime.now()) \
            .distinct() \
            .order_by('last_name')
        return designers


class ManufacturerManager(Manager):
    def with_published_rocking_chairs(self):
        manufacturers = self \
            .filter(rocking_chairs__published_at__lte=datetime.datetime.now()) \
            .distinct() \
            .order_by('name')
        return manufacturers
