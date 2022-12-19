from django.forms import ModelForm

from .models import Card


class CreateCardForm(ModelForm):
    """Creating a new card form"""
    class Meta:
        model = Card
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CreateCardForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form__control'
