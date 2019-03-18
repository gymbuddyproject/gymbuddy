# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-04 13:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gymbuddy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('Following', models.CharField(max_length=20)),
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('ProfilePicture', models.ImageField(blank=True, upload_to='profile_images')),
                ('Experience', models.CharField(max_length=30)),
                ('Height', models.IntegerField()),
                ('Weight', models.IntegerField()),
                ('DoB', models.DateField()),
                ('AboutMe', models.CharField(max_length=200, unique=True)),
                ('UserName', models.CharField(max_length=15)),
                ('Password', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30, unique=True)),
                ('GymID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymbuddy.Gym')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]