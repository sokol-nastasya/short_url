# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-12 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20180712_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='text',
            field=models.TextField(blank=True, default='Text', null=True),
        ),
    ]
