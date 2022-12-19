# Generated by Django 3.2 on 2022-12-19 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_auto_20221219_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='number',
            field=models.BigIntegerField(default=11111111111111, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 12, 47, 14, 650980), editable=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='usage_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 12, 47, 14, 651981), editable=False),
        ),
    ]
