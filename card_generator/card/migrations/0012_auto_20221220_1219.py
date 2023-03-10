# Generated by Django 3.2 on 2022-12-20 11:19

import card.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0011_auto_20221220_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='expiration_date',
            field=models.CharField(choices=[('2023-12-20 12:19:36', '2023-12-20 12:19:36 (1 year)'), ('2023-06-20 12:19:36', '2023-06-20 12:19:36 (6 months)'), ('2023-01-19 12:19:36', '2023-01-19 12:19:36 (30 days)')], default=card.models.default_expiration_date, max_length=255),
        ),
        migrations.AlterField(
            model_name='card',
            name='num_instances',
            field=models.IntegerField(default=1, verbose_name='Number of cards'),
        ),
        migrations.AlterField(
            model_name='card',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 12, 19, 36, 685978), editable=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='usage_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 12, 19, 36, 685978), editable=False),
        ),
    ]
