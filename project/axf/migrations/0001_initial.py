# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-04 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('long_name', models.CharField(max_length=150)),
                ('product_id', models.CharField(max_length=40)),
                ('store_nums', models.IntegerField()),
                ('specifics', models.CharField(max_length=40)),
                ('sort', models.IntegerField()),
                ('market_price', models.FloatField()),
                ('price', models.FloatField()),
                ('category_id', models.CharField(max_length=40)),
                ('child_cid', models.CharField(max_length=40)),
                ('img', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=200)),
                ('brand_id', models.CharField(max_length=40)),
                ('brand_name', models.CharField(max_length=200)),
                ('safe_day', models.CharField(max_length=20)),
                ('safe_unit', models.CharField(max_length=20)),
                ('safe_unit_desc', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='SliderShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('img', models.CharField(max_length=200)),
                ('sort', models.IntegerField()),
                ('trackid', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'slidershows',
            },
        ),
    ]