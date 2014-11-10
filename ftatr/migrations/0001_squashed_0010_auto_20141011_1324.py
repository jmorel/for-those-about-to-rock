# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ftatr.models


class Migration(migrations.Migration):

    replaces = [('ftatr', '0001_initial'), ('ftatr', '0002_auto_20141005_1444'), ('ftatr', '0003_auto_20141006_0835'), ('ftatr', '0004_auto_20141006_0838'), ('ftatr', '0005_auto_20141006_0847'), ('ftatr', '0006_rockingchair_published_at'), ('ftatr', '0007_rockingchair_price'), ('ftatr', '0008_auto_20141009_1943'), ('ftatr', '0009_auto_20141011_1317'), ('ftatr', '0010_auto_20141011_1324')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nationalities', models.ManyToManyField(to='ftatr.Country', blank=True)),
            ],
            options={
                'db_table': 'designer',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DesignerLink',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('url', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('designer', models.ForeignKey(to='ftatr.Designer')),
            ],
            options={
                'db_table': 'designer_link',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(null=True, to='ftatr.Country', blank=True)),
            ],
            options={
                'db_table': 'manufacturer',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ManufacturerLink',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('url', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('manufacturer', models.ForeignKey(to='ftatr.Manufacturer')),
            ],
            options={
                'db_table': 'manufacturer_link',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('currency', models.ForeignKey(to='ftatr.Currency')),
            ],
            options={
                'db_table': 'price',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PriceLink',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('url', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.ForeignKey(to='ftatr.Price')),
            ],
            options={
                'db_table': 'price_link',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RockingChair',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'rocking_chair',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='YearLink',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rocking_chair', models.ForeignKey(to='ftatr.RockingChair', related_name='year_links')),
            ],
            options={
                'db_table': 'year_link',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pricelink',
            name='rocking_chair',
            field=models.ForeignKey(to='ftatr.RockingChair', related_name='price_links'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='rocking_chair',
            field=models.ForeignKey(to='ftatr.RockingChair', related_name='pictures'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='manufacturerlink',
            name='rocking_chair',
            field=models.ForeignKey(to='ftatr.RockingChair', related_name='manufacturer_links'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='designerlink',
            name='rocking_chair',
            field=models.ForeignKey(to='ftatr.RockingChair', related_name='designer_links'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rocking_chair', models.ForeignKey(to='ftatr.RockingChair', related_name='links')),
            ],
            options={
                'db_table': 'rocking_chair_links',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rockingchair',
            name='designers',
            field=models.ManyToManyField(to='ftatr.Designer', blank=True, related_name='rocking_chairs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rockingchair',
            name='manufacturers',
            field=models.ManyToManyField(to='ftatr.Manufacturer', blank=True, related_name='rocking_chairs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rockingchair',
            name='year',
            field=models.IntegerField(max_length=4, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='designerlink',
            name='designer',
            field=models.ForeignKey(to='ftatr.Designer', related_name='links'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='manufacturerlink',
            name='manufacturer',
            field=models.ForeignKey(to='ftatr.Manufacturer', related_name='links'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(upload_to=ftatr.models.get_upload_to),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pricelink',
            name='price',
            field=models.ForeignKey(to='ftatr.Price', related_name='links'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='designerlink',
            name='url',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='manufacturerlink',
            name='url',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pricelink',
            name='url',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rockingchair',
            name='published_at',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='price',
            name='rocking_chair',
            field=models.OneToOneField(null=True, to='ftatr.RockingChair', blank=True, related_name='price'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rockingchair',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='designer',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=False,
        ),
    ]
