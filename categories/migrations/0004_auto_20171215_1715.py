# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-15 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_category_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name='Description (Markdown)'),
        ),
    ]
