from django.db import models
import datetime
from random import randint


def default_expiration_date():
    """Set a default expiration date equals 30 days"""
    return datetime.datetime.now() + datetime.timedelta(days=30)


def halfyear_expiration_date():
    """Set a expiration date equals 182 days (half a year)"""
    return datetime.datetime.now() + datetime.timedelta(days=182)


def year_expiration_date():
    """Set a expiration date equals a year"""
    return datetime.datetime.now() + datetime.timedelta(days=365)


class Card(models.Model):
    class ExpirationCardDate(models.TextChoices):
        year = "1", "1 year"
        halfyear = "2", "6 months"
        default = "3", "30 days"

    STATUS_CHOICES = (
        ('0', 'Non active'),
        ('1', 'Active'),
        ('2', 'Expired'),
    )
    # EXPIRATION_DATES = (
    #     (year_expiration_date, '1 year'),
    #     (halfyear_expiration_date, '6 months'),
    #     (default_expiration_date, '30 days'),
    # )
    series = models.CharField(max_length=3)
    number = models.CharField(max_length=16)
    release_date = models.DateTimeField(default=datetime.datetime.now(), editable=False)
    expiration_date = models.DateTimeField(default=default_expiration_date, choices=ExpirationCardDate.choices)
    usage_date = models.DateTimeField(default=datetime.datetime.now(), editable=False)
    status = models.CharField(max_length=10, default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)

