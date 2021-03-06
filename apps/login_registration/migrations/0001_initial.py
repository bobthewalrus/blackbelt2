# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 03:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasks', models.CharField(max_length=255)),
                ('date', models.DateField(default=datetime.datetime(2017, 1, 28, 19, 58, 27, 17898))),
                ('time', models.TimeField(default=datetime.datetime(2017, 1, 28, 19, 58, 27, 17918))),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('pw_hash', models.CharField(max_length=255)),
                ('dob', models.DateField(default=datetime.datetime(2017, 1, 28, 19, 58, 27, 12756))),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_registration.User'),
        ),
    ]
