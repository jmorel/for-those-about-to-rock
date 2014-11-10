# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nationalities', models.ManyToManyField(blank=True, to='ftatr.Country')),
            ],
            options={
                'db_table': 'designer',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DesignerLink',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
            name='Year',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('year', models.IntegerField(max_length=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rocking_chair', models.OneToOneField(to='ftatr.RockingChair', blank=True)),
            ],
            options={
                'db_table': 'year',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='YearLink',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('url', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rocking_chair', models.ForeignKey(null=True, to='ftatr.RockingChair')),
                ('year', models.ForeignKey(to='ftatr.Year')),
            ],
            options={
                'db_table': 'year_link',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pricelink',
            name='rocking_chair',
            field=models.ForeignKey(null=True, to='ftatr.RockingChair'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='price',
            name='rocking_chair',
            field=models.ForeignKey(to='ftatr.RockingChair'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='rocking_chair',
            field=models.ForeignKey(related_name='pictures', to='ftatr.RockingChair'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='manufacturerlink',
            name='rocking_chair',
            field=models.ForeignKey(null=True, to='ftatr.RockingChair'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='rocking_chairs',
            field=models.ManyToManyField(blank=True, related_name='manufacturers', to='ftatr.RockingChair'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='designerlink',
            name='rocking_chair',
            field=models.ForeignKey(null=True, to='ftatr.RockingChair'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='designer',
            name='rocking_chairs',
            field=models.ManyToManyField(blank=True, related_name='designers', to='ftatr.RockingChair'),
            preserve_default=True,
        ),
    ]
