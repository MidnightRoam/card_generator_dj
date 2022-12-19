from django.contrib import admin

from .models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('series', 'number', 'release_date', 'expiration_date', 'status', 'holder')
