# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('target_type', models.CharField(choices=[('rocking_chair', 'Rocking chair'), ('designer', 'Designer'), ('manufacturer', 'Manufacturer')], max_length=255)),
                ('target_slug', models.CharField(max_length=255)),
                ('attribute', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('status', models.CharField(default='new', choices=[('new', 'New'), ('rejected', 'Rejected'), ('accepted', 'Accepted')], max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('proposal', models.ForeignKey(to='contribution.Contribution', related_name='sources')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
