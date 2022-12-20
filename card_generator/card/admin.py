from django.contrib import admin

from .models import Card, Order


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('series', 'number', 'release_date', 'expiration_date', 'status', 'holder')
    search_fields = ('series', 'number', 'release_date', 'expiration_date', 'status')
    list_editable = ['status']

    # def save_model(self, request, obj, form, change):
    #     obj.save()
    #     Card.create_multiple_instances(obj.num_instances)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'card')
