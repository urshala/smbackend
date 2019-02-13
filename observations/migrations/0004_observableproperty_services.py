# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-09 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0069_unit_extensions'),
        ('observations', '0003_remove_observableproperty_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='observableproperty',
            name='services',
            field=models.ManyToManyField(related_name='observable_properties', to='services.Service'),
        ),
    ]
