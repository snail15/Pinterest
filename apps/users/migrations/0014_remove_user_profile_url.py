# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 19:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20170825_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_url',
        ),
    ]
