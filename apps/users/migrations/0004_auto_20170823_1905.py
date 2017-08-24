# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170823_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followings',
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='_user_following_+', to='users.User'),
        ),
    ]