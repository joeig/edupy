# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-02 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0011_remove_category_last_interaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharecontract',
            name='revoked',
            field=models.BooleanField(default=False),
        ),
    ]