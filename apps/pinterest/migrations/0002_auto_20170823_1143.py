# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='image',
            field=models.ImageField(blank=True, upload_to='pins', verbose_name='jpg'),
        ),
    ]