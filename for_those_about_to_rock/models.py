from django.db import models


class RockingChair(models.Model):
    name = models.CharField(max_length=255)

    # inversed relationships:
    # * designer_set
    # * manufacturer_set
    # * price_set
    # * year
    # * picture_set

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    # publication planning management
    # todo: task to auto publish planned publication
    # is_published = models.BooleanField(default=False)
    # published_at = models.DateTimeField(null=True, default=None)

    class Meta:
        db_table = 'rocking_chair'


class Picture(models.Model):
    path = models.CharField(max_length=255)

    rocking_chair = models.ForeignKey('RockingChair')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'picture'


class Price(models.Model):
    amount = models.FloatField()

    rocking_chair = models.ForeignKey('RockingChair')
    currency = models.ForeignKey('Currency')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'price'


class Designer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField(blank=True, null=True)

    rocking_chairs = models.ManyToManyField('RockingChair', related_name='designers')
    nationalities = models.ManyToManyField('Country', blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'designer'


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    country = models.ForeignKey('Country', blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'manufacturer'


class Year(models.Model):
    year = models.IntegerField(max_length=4)

    rocking_chair = models.OneToOneField('RockingChair')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'year'


class Link(models.Model):
    url = models.TextField()

    rocking_chair = models.ForeignKey('RockingChair', null=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DesignerLink(Link):
    designer = models.ForeignKey('Designer')

    class Meta:
        db_table = 'designer_link'


class ManufacturerLink(Link):
    manufacturer = models.ForeignKey('Manufacturer')

    class Meta:
        db_table = 'manufacturer_link'


class PriceLink(Link):
    price = models.ForeignKey('Price')

    class Meta:
        db_table = 'price_link'


class YearLink(Link):
    year = models.ForeignKey('Year')

    class Meta:
        db_table = 'year_link'


class Currency(models.Model):
    name = models.TextField()
    code = models.TextField()

    class Meta:
        db_table = 'currency'


class Country(models.Model):
    name = models.TextField()
    code = models.TextField()

    class Meta:
        db_table = 'country'