# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ftatr', '0007_rockingchair_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rockingchair',
            name='price',
        ),
        migrations.AddField(
            model_name='price',
            name='rocking_chair',
            field=models.OneToOneField(to='ftatr.RockingChair', blank=True, null=True),
            preserve_default=True,
        ),
    ]
