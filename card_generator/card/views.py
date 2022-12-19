from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Card
from .forms import CreateCardForm


class IndexView(ListView):
    model = Card
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cards'] = Card.objects.filter(status='Active')
        return context


class GenerateCardView(CreateView):
    template_name = 'card_generator.html'
    success_url = reverse_lazy('index')
    form_class = CreateCardForm

