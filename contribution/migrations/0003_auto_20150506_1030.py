# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contribution', '0002_auto_20150505_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='source',
            old_name='proposal',
            new_name='contribution',
        ),
    ]
