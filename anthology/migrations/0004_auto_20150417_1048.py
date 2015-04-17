# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anthology', '0003_auto_20150417_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='priority',
            field=models.SmallIntegerField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
