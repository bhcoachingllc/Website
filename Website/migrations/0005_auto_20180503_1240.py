# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0004_user_roles_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_roles',
            name='exp_date',
            field=models.DateField(blank=True),
        ),
    ]
