# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-25 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20181213_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleinfo',
            name='taginfo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.TagInfo', verbose_name='所属标签'),
        ),
        migrations.AlterField(
            model_name='articleinfo',
            name='image',
            field=models.ImageField(blank=True, default='article/default1.jpg', max_length=200, null=True, upload_to='article/%y/%m/%d', verbose_name='封面'),
        ),
    ]
