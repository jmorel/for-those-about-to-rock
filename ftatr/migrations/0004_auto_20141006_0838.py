# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ftatr', '0003_auto_20141006_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rockingchair',
            name='price',
            field=models.OneToOneField(blank=True, to='ftatr.Price', null=True, related_name='rocking_chair'),
        ),
    ]
