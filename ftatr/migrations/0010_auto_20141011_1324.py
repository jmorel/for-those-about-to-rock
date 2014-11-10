# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ftatr', '0009_auto_20141011_1317'),
    ]

    operations = [
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
