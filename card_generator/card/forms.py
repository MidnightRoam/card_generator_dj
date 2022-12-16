from django.forms import ModelForm

from .models import Card


class QuizForm(ModelForm):
    class Meta:
        model = Card
        fields = "__all__"
