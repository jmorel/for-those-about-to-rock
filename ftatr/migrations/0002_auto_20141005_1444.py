# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ftatr.models


class Migration(migrations.Migration):

    dependencies = [
        ('ftatr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rocking_chair', models.ForeignKey(related_name='links', to='ftatr.RockingChair')),
            ],
            options={
                'db_table': 'rocking_chair_links',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='designer',
            name='rocking_chairs',
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='rocking_chairs',
        ),
        migrations.RemoveField(
            model_name='price',
            name='rocking_chair',
        ),
        migrations.RemoveField(
            model_name='year',
            name='rocking_chair',
        ),
        migrations.AddField(
            model_name='rockingchair',
            name='designers',
            field=models.ManyToManyField(blank=True, to='ftatr.Designer', related_name='rocking_chairs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rockingchair',
            name='manufacturers',
            field=models.ManyToManyField(blank=True, to='ftatr.Manufacturer', related_name='rocking_chairs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rockingchair',
            name='price',
            field=models.ForeignKey(related_name='rocking_chairs', blank=True, to='ftatr.Price', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rockingchair',
            name='year',
            field=models.ForeignKey(related_name='rocking_chairs', blank=True, to='ftatr.Year', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='designerlink',
            name='designer',
            field=models.ForeignKey(related_name='links', to='ftatr.Designer'),
        ),
        migrations.AlterField(
            model_name='designerlink',
            name='rocking_chair',
            field=models.ForeignKey(related_name='designer_links', to='ftatr.RockingChair'),
        ),
        migrations.AlterField(
            model_name='manufacturerlink',
            name='manufacturer',
            field=models.ForeignKey(related_name='links', to='ftatr.Manufacturer'),
        ),
        migrations.AlterField(
            model_name='manufacturerlink',
            name='rocking_chair',
            field=models.ForeignKey(related_name='manufacturer_links', to='ftatr.RockingChair'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(upload_to=ftatr.models.get_upload_to),
        ),
        migrations.AlterField(
            model_name='pricelink',
            name='price',
            field=models.ForeignKey(related_name='links', to='ftatr.Price'),
        ),
        migrations.AlterField(
            model_name='pricelink',
            name='rocking_chair',
            field=models.ForeignKey(related_name='price_links', to='ftatr.RockingChair'),
        ),
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.IntegerField(max_length=4, unique=True),
        ),
        migrations.AlterField(
            model_name='yearlink',
            name='rocking_chair',
            field=models.ForeignKey(related_name='year_links', to='ftatr.RockingChair'),
        ),
        migrations.AlterField(
            model_name='yearlink',
            name='year',
            field=models.ForeignKey(related_name='links', to='ftatr.Year'),
        ),
    ]
