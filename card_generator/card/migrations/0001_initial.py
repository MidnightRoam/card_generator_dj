# Generated by Django 3.2 on 2022-12-16 15:23

import card.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.IntegerField()),
                ('number', models.IntegerField()),
                ('release_date', models.DateTimeField(default=datetime.datetime(2022, 12, 16, 16, 23, 30, 104247), editable=False)),
                ('expiration_date', models.DateTimeField(choices=[(card.models.year_expiration_date, '1 year'), (card.models.halfyear_expiration_date, '6 months'), (card.models.default_expiration_date, '30 days')], default=card.models.default_expiration_date)),
                ('usage_date', models.DateTimeField(default=datetime.datetime(2022, 12, 16, 16, 23, 30, 104247), editable=False)),
                ('status', models.CharField(choices=[('0', 'Non active'), ('1', 'Active'), ('2', 'Expired')], default='0', max_length=10)),
            ],
        ),
    ]
