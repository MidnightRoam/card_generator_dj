from django.db import models
from django.urls import reverse
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User


def default_expiration_date():
    """Set a default expiration date equals 30 days"""
    date = datetime.datetime.now() + datetime.timedelta(days=30)
    format_date = date.strftime("%Y-%m-%d %H:%M:%S")
    return format_date


def halfyear_expiration_date():
    """Set a expiration date equals 182 days (half a year)"""
    date = datetime.datetime.now() + datetime.timedelta(days=182)
    format_date = date.strftime("%Y-%m-%d %H:%M:%S")
    return format_date


def year_expiration_date():
    """Set a expiration date equals a year"""
    date = datetime.datetime.now() + datetime.timedelta(days=365)
    format_date = date.strftime("%Y-%m-%d %H:%M:%S")
    return format_date


class Card(models.Model):
    """Card model"""
    class ExpirationCardDate(models.TextChoices):
        """Text choices class for a expiration_date field"""
        year = year_expiration_date(), f"{year_expiration_date()} (1 year)"
        halfyear = halfyear_expiration_date(), f"{halfyear_expiration_date()} (6 months)"
        default = default_expiration_date(), f"{default_expiration_date()} (30 days)"

    class StatusCard(models.TextChoices):
        """Text choices class for a status field"""
        non_active = 'Non active',
        active = 'Active',
        expired = 'Expired'

    series = models.IntegerField(unique=True,
                                 default=10,
                                 editable=False)
    number = models.BigIntegerField(unique=True,
                                    default=10000000000000,
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
    num_instances = models.IntegerField('Number of cards',
                                        default=1,
                                        validators=[
                                            MaxValueValidator(20),
                                            MinValueValidator(1)
                                        ])

    def save(self, *args, **kwargs):
        """Increment unique card series and card number at creating a new card"""
        cards = Card.objects.all()
        default_card_number = 1000000000000

        if cards.exists() and self._state.adding:   # self._state.adding ?????????????????? ?????????????????????? ???????????????? ???????????? ?? ????????????
            # ???????????????? ??????????, ?? ???? ???????????? ?????????? ?????? ???? ????????????????????
            last_number = cards.latest('number')
            self.number = int(last_number.number) + default_card_number + 1

            last_series = cards.latest('series')
            self.series = int(last_series.series) + 1
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Returns personal url for a card profile"""
        return reverse('profile', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.number)

    def check_expiration(self):
        """Check for expired cards function"""
        # Convert the expiration date string to a datetime object
        expiration_date = datetime.datetime.strptime(self.expiration_date, '%Y-%m-%d %H:%M:%S')

        # Check if the expiration date has passed
        if datetime.datetime.now() > expiration_date:
            # Update the status field to "Expired"
            self.status = self.StatusCard.choices[2][2]
            self.save()


class Order(models.Model):
    """Orders model"""
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
