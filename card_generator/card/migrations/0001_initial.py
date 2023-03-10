# Generated by Django 3.2 on 2022-12-19 11:22

import card.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=3)),
                ('number', models.IntegerField(default=1000000000000000, max_length=16, unique=True)),
                ('release_date', models.DateTimeField(default=datetime.datetime(2022, 12, 19, 12, 22, 37, 347359), editable=False)),
                ('expiration_date', models.CharField(choices=[('1 year', '1 year'), ('6 months', '6 months'), ('30 days', '30 days')], default=card.models.default_expiration_date, max_length=255)),
                ('usage_date', models.DateTimeField(default=datetime.datetime(2022, 12, 19, 12, 22, 37, 347359), editable=False)),
                ('status', models.CharField(choices=[('Non active', 'Non Active'), ('Active', 'Active'), ('Expired', 'Expired')], default='Active', max_length=10)),
                ('holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
