# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20170825_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default="{%static 'users/img/profile.jpg'%}", upload_to='users'),
        ),
    ]
