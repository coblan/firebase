# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-04 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tag_order', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(default='', max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image_order', models.CharField(max_length=400)),
                ('app', models.ManyToManyField(to='storage.App')),
            ],
        ),
        migrations.AddField(
            model_name='graph',
            name='tag',
            field=models.ManyToManyField(to='storage.Tag'),
        ),
    ]