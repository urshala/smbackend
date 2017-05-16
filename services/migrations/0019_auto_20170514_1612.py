# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 13:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_auto_20170514_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='root_ontologytreenodes',
            field=models.CharField(max_length=50, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]