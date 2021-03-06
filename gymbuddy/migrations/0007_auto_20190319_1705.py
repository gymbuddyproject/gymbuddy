# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-19 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import gymbuddy.models


class Migration(migrations.Migration):

    dependencies = [
        ('gymbuddy', '0006_auto_20190318_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ProfilePicture',
            field=models.ImageField(blank=True, upload_to=gymbuddy.models.profile_directory_path),
        ),
        migrations.AlterField(
            model_name='progresspics',
            name='Photo',
            field=models.ImageField(upload_to=gymbuddy.models.progress_directory_path),
        ),
    ]
