# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 14:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_index1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='index1',
        ),
    ]
