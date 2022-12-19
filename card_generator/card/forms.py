from django.forms import ModelForm

from .models import Card


class CreateCardForm(ModelForm):
    """Creating a new card form"""
    class Meta:
        model = Card
        fields = "__all__"
