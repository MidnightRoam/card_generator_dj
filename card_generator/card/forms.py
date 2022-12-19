from django.forms import ModelForm

from .models import Card


class CreateCardForm(ModelForm):
    class Meta:
        model = Card
        fields = "__all__"
