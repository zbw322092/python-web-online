# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-14 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_course_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default='backend', max_length=20, verbose_name='\u8bfe\u7a0b\u7c7b\u522b'),
        ),
    ]
