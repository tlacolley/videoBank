# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_bank', '0002_auto_20181105_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='length',
            field=models.CharField(max_length=50),
        ),
    ]
