# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-01 00:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20171130_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerform',
            name='owner',
        ),
    ]
