# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contribution', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='created_at',
            field=models.DateTimeField(default='2015-05-05 12:12', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contribution',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 5, 11, 9, 51, 448707), auto_now=True),
            preserve_default=False,
        ),
    ]
