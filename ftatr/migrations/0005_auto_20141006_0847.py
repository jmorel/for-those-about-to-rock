# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ftatr', '0004_auto_20141006_0838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rockingchair',
            name='price',
        ),
        migrations.AlterField(
            model_name='designerlink',
            name='url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='manufacturerlink',
            name='url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pricelink',
            name='url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='yearlink',
            name='url',
            field=models.CharField(max_length=255),
        ),
    ]
