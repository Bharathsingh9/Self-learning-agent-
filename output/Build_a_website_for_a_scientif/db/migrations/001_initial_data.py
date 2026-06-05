python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('contenttypes', '0002_remove_ct_field_from_generic_relation'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalculatorPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(choices=[('light', 'Light Theme'), ('dark', 'Dark Theme')], default='light', max_length=10)),
                ('units', models.CharField(choices=[('metric', 'Metric Units'), ('imperial', 'Imperial Units')], default='metric', max_length=10)),
                ('last_calculator_version', models.CharField(max_length=10)),
                ('last_app_update', models.DateTimeField(auto_now=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=models.CASCADE, to='users.UserProfile')),
                ('polymorphic_ctype',
                models.ForeignKey(
                    editable=False,
                    null=True,
                    on_delete=models.CASCADE,
                    related_name='+',
                    to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CalculatorHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', models.CharField(max_length=100)),
                ('result', models.CharField(max_length=30)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=models.CASCADE, to='users.UserProfile')),
                ('polymorphic_ctype',
                models.ForeignKey(
                    editable=False,
                    null=True,
                    on_delete=models.CASCADE,
                    related_name='+',
                    to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]


This migration creates two tables (`CalculatorPreference` and `CalculatorHistory`) with their respective fields and relationships to the `UserProfile` model and generic foreign keys to the `ContentType` model for polymorphic relationships.