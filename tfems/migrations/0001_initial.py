# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-29 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_address', models.CharField(max_length=100)),
                ('emp_phone', models.CharField(max_length=13)),
                ('emp_email', models.CharField(max_length=100)),
                ('emp_designation', models.CharField(max_length=100)),
                ('emp_joining_date', models.DateField()),
                ('emp_working_hours', models.IntegerField()),
            ],
        ),
    ]