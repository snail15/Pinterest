# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170823_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.ImageField(default='pinterest/img/profile.jpg', upload_to='users'),
        ),
    ]