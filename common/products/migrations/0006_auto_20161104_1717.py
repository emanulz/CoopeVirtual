# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 23:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20161104_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company', verbose_name='Compa\xf1\xeda'),
        ),
    ]
