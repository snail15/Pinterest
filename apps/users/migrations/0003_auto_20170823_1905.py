# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(related_name='_user_followings_+', to='users.User'),
        ),
    ]
