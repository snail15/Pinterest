# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 00:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest', '0009_merge_20170824_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basecomment',
            name='title',
        ),
        migrations.AlterField(
            model_name='boardcomment',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='pinterest.Board'),
        ),
        migrations.AlterField(
            model_name='pincomment',
            name='pin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='pinterest.Pin'),
        ),
    ]
