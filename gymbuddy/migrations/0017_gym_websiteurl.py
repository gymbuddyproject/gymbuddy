# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-20 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymbuddy', '0016_auto_20190320_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='gym',
            name='WebsiteURL',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]