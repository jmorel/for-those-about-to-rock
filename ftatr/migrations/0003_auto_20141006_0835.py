# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ftatr', '0002_auto_20141005_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yearlink',
            name='year',
        ),
        migrations.AlterField(
            model_name='rockingchair',
            name='year',
            field=models.IntegerField(null=True, blank=True, max_length=4),
        ),
        migrations.DeleteModel(
            name='Year',
        ),
    ]
