# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-20 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymbuddy', '0021_auto_20190320_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
