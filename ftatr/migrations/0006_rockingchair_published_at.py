# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ftatr', '0005_auto_20141006_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='rockingchair',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
