import datetime
from django.db import models
from ftatr.settings import MEDIA_ROOT
import hashlib
import os


class RockingChair(models.Model):
    class Meta:
        db_table = 'rocking_chair'

    name = models.CharField(max_length=255)

    year = models.ForeignKey('Year', related_name='rocking_chairs', blank=True, null=True)
    price = models.ForeignKey('Price', related_name='rocking_chairs', blank=True, null=True)
    designers = models.ManyToManyField('Designer', related_name='rocking_chairs', blank=True)
    manufacturers = models.ManyToManyField('Manufacturer', related_name='rocking_chairs', blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    # publication planning management
    # todo: task to auto publish planned publication
    # is_published = models.BooleanField(default=False)
    # published_at = models.DateTimeField(null=True, default=None)

    def __str__(self):
        return self.name


def get_upload_to(instance, filename):
    md5sum = hashlib.md5()
    md5sum.update(filename.encode('utf-8'))
    md5sum.update(str(datetime.datetime.now()).encode('utf-8'))
    md5sum = md5sum.hexdigest()
    return os.path.join(MEDIA_ROOT, md5sum[:1], md5sum[:2], md5sum)


class Picture(models.Model):
    class Meta:
        db_table = 'picture'

    picture = models.ImageField(upload_to=get_upload_to)

    rocking_chair = models.ForeignKey('RockingChair', related_name='pictures')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


class Price(models.Model):
    class Meta:
        db_table = 'price'

    amount = models.FloatField()

    currency = models.ForeignKey('Currency')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.amount, self.currency.code)


class Designer(models.Model):
    class Meta:
        db_table = 'designer'

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField(blank=True, null=True)

    nationalities = models.ManyToManyField('Country', blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Manufacturer(models.Model):
    class Meta:
        db_table = 'manufacturer'

    name = models.CharField(max_length=255)

    country = models.ForeignKey('Country', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Year(models.Model):
    class Meta:
        db_table = 'year'

    year = models.IntegerField(max_length=4, unique=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.year)


class Link(models.Model):
    class Meta:
        db_table = 'rocking_chair_links'

    url = models.TextField()

    rocking_chair = models.ForeignKey('RockingChair', related_name='links')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


class DesignerLink(models.Model):
    url = models.TextField()

    rocking_chair = models.ForeignKey('RockingChair', related_name='designer_links')
    designer = models.ForeignKey('Designer', related_name='links')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'designer_link'


class ManufacturerLink(models.Model):
    url = models.TextField()

    rocking_chair = models.ForeignKey('RockingChair', related_name='manufacturer_links')
    manufacturer = models.ForeignKey('Manufacturer', related_name='links')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'manufacturer_link'


class PriceLink(models.Model):
    url = models.TextField()

    rocking_chair = models.ForeignKey('RockingChair', related_name='price_links')
    price = models.ForeignKey('Price', related_name='links')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'price_link'


class YearLink(models.Model):
    url = models.TextField()

    rocking_chair = models.ForeignKey('RockingChair', related_name='year_links')
    year = models.ForeignKey('Year', related_name='links')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'year_link'


class Currency(models.Model):
    class Meta:
        db_table = 'currency'

    name = models.TextField()
    code = models.TextField()

    def __str__(self):
        return self.name


class Country(models.Model):
    class Meta:
        db_table = 'country'

    name = models.TextField()
    code = models.TextField()

    def __str__(self):
        return self.name
