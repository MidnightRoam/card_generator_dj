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

    def save(self):
        # Get the number of instances from the form data
        num_instances = self.cleaned_data['num_instances']

        # Create the instances using a loop
        for i in range(num_instances):
            instance = Card(**self.cleaned_data)
            instance.save()
