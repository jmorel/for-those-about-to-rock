# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ftatr', '0008_auto_20141009_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='rockingchair',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='price',
            name='rocking_chair',
            field=models.OneToOneField(null=True, blank=True, to='ftatr.RockingChair', related_name='price'),
        ),
    ]
