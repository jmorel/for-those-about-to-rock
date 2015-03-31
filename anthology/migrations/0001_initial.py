# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import anthology.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.TextField()),
                ('code', models.TextField()),
            ],
            options={
                'db_table': 'country',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.TextField()),
                ('code', models.TextField()),
            ],
            options={
                'db_table': 'currency',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('portrait', models.ImageField(null=True, blank=True, upload_to=anthology.models.Designer.get_upload_to)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nationalities', models.ManyToManyField(to='anthology.Country', blank=True)),
            ],
            options={
                'db_table': 'designer',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DesignerLink',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('designer', models.ForeignKey(to='anthology.Designer', related_name='links')),
            ],
            options={
                'db_table': 'designer_link',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'rocking_chair_links',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(null=True, blank=True, upload_to=anthology.models.Manufacturer.get_upload_to)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(null=True, blank=True, to='anthology.Country')),
            ],
            options={
                'db_table': 'manufacturer',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ManufacturerLink',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('manufacturer', models.ForeignKey(to='anthology.Manufacturer', related_name='links')),
            ],
            options={
                'db_table': 'manufacturer_link',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('picture', models.ImageField(upload_to=anthology.models.RockingChair.get_upload_to)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'picture',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('currency', models.ForeignKey(to='anthology.Currency')),
            ],
            options={
                'db_table': 'price',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PriceLink',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.ForeignKey(to='anthology.Price', related_name='links')),
            ],
            options={
                'db_table': 'price_link',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RockingChair',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', models.IntegerField(null=True, blank=True, max_length=4)),
                ('slug', models.SlugField(unique=True)),
                ('published_at', models.DateTimeField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('designers', models.ManyToManyField(related_name='rocking_chairs', to='anthology.Designer', blank=True)),
                ('manufacturers', models.ManyToManyField(related_name='rocking_chairs', to='anthology.Manufacturer', blank=True)),
            ],
            options={
                'db_table': 'rocking_chair',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='YearLink',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rocking_chair', models.ForeignKey(to='anthology.RockingChair', related_name='year_links')),
            ],
            options={
                'db_table': 'year_link',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pricelink',
            name='rocking_chair',
            field=models.ForeignKey(to='anthology.RockingChair', related_name='price_links'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='price',
            name='rocking_chair',
            field=models.OneToOneField(related_name='price', null=True, blank=True, to='anthology.RockingChair'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='rocking_chair',
            field=models.ForeignKey(to='anthology.RockingChair', related_name='pictures'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='manufacturerlink',
            name='rocking_chair',
            field=models.ForeignKey(to='anthology.RockingChair', related_name='manufacturer_links'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='link',
            name='rocking_chair',
            field=models.ForeignKey(to='anthology.RockingChair', related_name='links'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='designerlink',
            name='rocking_chair',
            field=models.ForeignKey(to='anthology.RockingChair', related_name='designer_links'),
            preserve_default=True,
        ),
    ]
