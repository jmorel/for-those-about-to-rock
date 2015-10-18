# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anthology', '0005_auto_20150417_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('target_type', models.CharField(choices=[('rocking_chair', 'Rocking chair'), ('designer', 'Designer'), ('manufacturer', 'Manufacturer')], max_length=15)),
                ('target_slug', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('new', 'New'), ('closed', 'Closed')], default='new', max_length=10)),
                ('created_at', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
