# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 11:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_bank', '0003_auto_20181105_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='picture',
        ),
    ]
