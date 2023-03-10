# Generated by Django 3.2 on 2022-12-20 11:08

import card.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0010_auto_20221219_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='num_instances',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='card',
            name='expiration_date',
            field=models.CharField(choices=[('2023-12-20 12:08:40', '2023-12-20 12:08:40 (1 year)'), ('2023-06-20 12:08:40', '2023-06-20 12:08:40 (6 months)'), ('2023-01-19 12:08:40', '2023-01-19 12:08:40 (30 days)')], default=card.models.default_expiration_date, max_length=255),
        ),
        migrations.AlterField(
            model_name='card',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 12, 8, 40, 389082), editable=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='usage_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 12, 8, 40, 389082), editable=False),
        ),
    ]
