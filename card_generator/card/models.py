from django.db import models
import datetime

from django.contrib.auth.models import User


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
        """Text choices class for a expiration_date field"""
        year = "1 year", "1 year"
        halfyear = "6 months", "6 months"
        default = "30 days", "30 days"

    class StatusCard(models.TextChoices):
        """Text choices class for a status field"""
        non_active = 'Non active',
        active = 'Active',
        expired = 'Expired'

    series = models.IntegerField(unique=True,
                                 default=10,
                                 editable=False)
    number = models.IntegerField(unique=True,
                                 default=00000000000000,
                                 editable=False)
    release_date = models.DateTimeField(default=datetime.datetime.now(),
                                        editable=False)
    expiration_date = models.CharField(max_length=255,
                                       default=default_expiration_date,
                                       choices=ExpirationCardDate.choices)
    usage_date = models.DateTimeField(default=datetime.datetime.now(),
                                      editable=False)
    status = models.CharField(max_length=10,
                              default=StatusCard.choices[1][1],
                              choices=StatusCard.choices)
    holder = models.ForeignKey(User,
                               on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """Increment unique card series and card number at creating a new card"""
        cards = Card.objects.all()

        if cards.exists() and self._state.adding:   # self._state.adding позволяет увеличивать значение только в момент
            # создания карты, и не делать этого при её обновлении
            last_number = cards.latest('number')
            self.number = int(last_number.number) + 1

            last_series = cards.latest('series')
            self.series = int(last_series.series) + 1
        super().save(*args, **kwargs)
