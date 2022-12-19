# Generated by Django 3.2 on 2022-12-19 13:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('card', '0006_auto_20221219_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 14, 45, 53, 296870), editable=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='usage_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 14, 45, 53, 296870), editable=False),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
