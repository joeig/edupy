# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-11 08:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cards', '0013_card_postpone_until'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CardPlacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=1, verbose_name='Area')),
                ('last_interaction', models.DateTimeField(auto_now_add=True)),
                ('postpone_until', models.DateTimeField(default=django.utils.timezone.now)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_placements', to='cards.Card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='cardplacement',
            unique_together=set([('card', 'user')]),
        ),
    ]
