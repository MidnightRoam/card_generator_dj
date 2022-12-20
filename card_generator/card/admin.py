from django.contrib import admin

from .models import Card, Order


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('series', 'number', 'release_date', 'expiration_date', 'status', 'holder')
    search_fields = ('series', 'number', 'release_date', 'expiration_date', 'status')
    list_editable = ['status']

    def save_model(self, request, obj, form, change):
        # Get the number of instances and the valid data from the form
        num_instances = form.cleaned_data['num_instances']
        valid_data = {
            'series': form.cleaned_data.get('series'),
            'number': form.cleaned_data.get('number'),
            'expiration_date': form.cleaned_data.get('expiration_date'),
            'status': form.cleaned_data.get('status'),
            'holder': form.cleaned_data.get('holder'),
            'num_instances': form.cleaned_data.get('num_instances')
        }
        # Save the object using the default save method
        obj.save()

        # Create the additional instances using a loop
        for i in range(num_instances - 1):
            instance = Card(**valid_data)
            instance.save()


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'card')
