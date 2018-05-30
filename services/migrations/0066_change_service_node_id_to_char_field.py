# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-30 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0065_tune_unit_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicenode',
            name='keywords',
            field=models.ManyToManyField(db_constraint=False, to='services.Keyword'),
        ),
        migrations.AlterField(
            model_name='servicenode',
            name='parent',
            field=mptt.fields.TreeForeignKey(db_constraint=False, null=True,
                                             on_delete=django.db.models.deletion.CASCADE, related_name='children',
                                             to='services.ServiceNode'),
        ),
        migrations.AlterField(
            model_name='servicenode',
            name='related_services',
            field=models.ManyToManyField(db_constraint=False, to='services.Service'),
        ),
        migrations.AlterField(
            model_name='servicenodeunitcount',
            name='service_node',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='unit_counts', to='services.ServiceNode'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='service_nodes',
            field=models.ManyToManyField(db_constraint=False, related_name='units', to='services.ServiceNode'),
        ),
        migrations.AlterField(
            model_name='servicemapping',
            name='node_id',
            field=models.ForeignKey(db_constraint=False, to='services.ServiceNode'),
        ),
        migrations.AlterField(
            model_name='servicenode',
            name='id',
            field=models.CharField(blank=True, db_index=True, max_length=200, primary_key=True, serialize=False),
        ),

        migrations.RunSQL("ALTER TABLE services_servicenode_keywords ALTER COLUMN servicenode_id TYPE varchar(200);"),
        migrations.RunSQL("ALTER TABLE services_servicenode ALTER COLUMN parent_id TYPE varchar(200);"),
        migrations.RunSQL("ALTER TABLE services_servicenode_related_services ALTER COLUMN servicenode_id TYPE varchar(200);"),
        migrations.RunSQL("ALTER TABLE services_servicenodeunitcount ALTER COLUMN service_node_id TYPE varchar(200);"),
        migrations.RunSQL("ALTER TABLE services_unit_service_nodes ALTER COLUMN servicenode_id TYPE varchar(200);"),
        migrations.RunSQL("ALTER TABLE services_servicemapping ALTER COLUMN node_id_id TYPE varchar(200);"),

        migrations.AlterField(
            model_name='servicenode',
            name='keywords',
            field=models.ManyToManyField(to='services.Keyword'),
        ),
        migrations.AlterField(
            model_name='servicenode',
            name='parent',
            field=mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='services.ServiceNode'),
        ),
        migrations.AlterField(
            model_name='servicenode',
            name='related_services',
            field=models.ManyToManyField(to='services.Service'),
        ),
        migrations.AlterField(
            model_name='servicenodeunitcount',
            name='service_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_counts', to='services.ServiceNode'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='service_nodes',
            field=models.ManyToManyField(related_name='units', to='services.ServiceNode'),
        ),
        migrations.AlterField(
            model_name='servicemapping',
            name='node_id',
            field=models.ForeignKey(to='services.ServiceNode'),
        ),
    ]
