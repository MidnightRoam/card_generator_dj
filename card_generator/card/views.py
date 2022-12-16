from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Card


class IndexView(ListView):
    model = Card
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cards'] = Card.objects.all()
        return context


class GenerateCardView(CreateView):
    template_name = 'card_generator.html'
    success_url = reverse_lazy('index')
    model = Card
    fields = '__all__'

