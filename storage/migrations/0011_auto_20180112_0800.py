# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-12 08:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0010_auto_20180112_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graph',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 12, 8, 0, 15, 291632, tzinfo=utc), verbose_name='upload date'),
        ),
        migrations.AlterField(
            model_name='package',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='package',
            name='thumb_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
