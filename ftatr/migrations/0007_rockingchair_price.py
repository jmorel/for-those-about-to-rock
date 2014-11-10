# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ftatr', '0006_rockingchair_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='rockingchair',
            name='price',
            field=models.OneToOneField(null=True, to='ftatr.Price', blank=True),
            preserve_default=True,
        ),
    ]
