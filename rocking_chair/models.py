import datetime
from django.db import models
import hashlib
import os


class RockingChair(models.Model):
    class Meta:
        db_table = 'rocking_chair'

    name = models.CharField(max_length=255)
    year = models.IntegerField(max_length=4, null=True, blank=True)

    # price = models.OneToOneField('Price', blank=True, null=True)
    designers = models.ManyToManyField('Designer', related_name='rocking_chairs', blank=True)
    manufacturers = models.ManyToManyField('Manufacturer', related_name='rocking_chairs', blank=True)

    slug = models.SlugField(unique=True)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_published(self):
        return self.published_at and (self.published_at < datetime.datetime.now())

    @property
    def twitter_text(self):
        designers = list(self.designers.all())

        if not designers:
            return self.name

        authors = ', '.join([designer.full_name for designer in designers[:-1]])
        if authors:
            authors = "{} and {}".format(authors, designers[-1].full_name)
        else:
            authors = designers[-1].full_name

        return "{} by {}".format(self.name, authors)


def get_upload_to(self, filename):
    slug = self.rocking_chair.slug
    name, extension = os.path.splitext(filename)
    md5sum = hashlib.md5()
    md5sum.update(filename.encode('utf-8'))
    md5sum.update(str(datetime.datetime.now()).encode('utf-8'))
    md5sum = md5sum.hexdigest()
    return os.path.join('rocking-chairs', slug, md5sum+extension)


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

    rocking_chair = models.OneToOneField('RockingChair', related_name='price', blank=True, null=True)
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

    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name).strip()


class Manufacturer(models.Model):
    class Meta:
        db_table = 'manufacturer'

    name = models.CharField(max_length=255)

    country = models.ForeignKey('Country', blank=True, null=True)

    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Link(models.Model):
    class Meta:
        db_table = 'rocking_chair_links'

    url = models.CharField(max_length=255)

    rocking_chair = models.ForeignKey('RockingChair', related_name='links')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


class DesignerLink(models.Model):
    class Meta:
        db_table = 'designer_link'

    url = models.CharField(max_length=255)

    rocking_chair = models.ForeignKey('RockingChair', related_name='designer_links')
    designer = models.ForeignKey('Designer', related_name='links')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


class ManufacturerLink(models.Model):
    class Meta:
        db_table = 'manufacturer_link'

    url = models.CharField(max_length=255)

    rocking_chair = models.ForeignKey('RockingChair', related_name='manufacturer_links')
    manufacturer = models.ForeignKey('Manufacturer', related_name='links')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


class PriceLink(models.Model):
    class Meta:
        db_table = 'price_link'

    url = models.CharField(max_length=255)

    rocking_chair = models.ForeignKey('RockingChair', related_name='price_links')
    price = models.ForeignKey('Price', related_name='links')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


class YearLink(models.Model):
    class Meta:
        db_table = 'year_link'

    url = models.CharField(max_length=255)

    rocking_chair = models.ForeignKey('RockingChair', related_name='year_links')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


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
