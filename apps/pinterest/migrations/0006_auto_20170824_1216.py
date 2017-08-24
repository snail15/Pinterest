# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170823_1942'),
        ('pinterest', '0005_merge_20170824_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('followers', models.ManyToManyField(blank=True, related_name='topics_followed', to='users.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='pin',
            name='topic',
        ),
        migrations.AddField(
            model_name='board',
            name='topic',
            field=models.ManyToManyField(related_name='boards', to='pinterest.Topic'),
        ),
        migrations.AddField(
            model_name='pin',
            name='topic',
            field=models.ManyToManyField(related_name='pins', to='pinterest.Topic'),
        ),
    ]