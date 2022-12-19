from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.models import User

from .models import Card, Order
from .forms import CreateCardForm


class IndexView(ListView):
    """List of cards filtered by card status is Active"""
    model = Card
    template_name = 'pages/index.html'
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        p = Paginator(Card.objects.filter(status='Active'), self.paginate_by)
        context['cards'] = p.page(context['page_obj'].number)
        return context


class GenerateCardView(CreateView):
    """Create view for a generation card form without a admin panel"""
    template_name = 'pages/card_generator.html'
    success_url = reverse_lazy('index')
    form_class = CreateCardForm


class CardDetailView(DetailView):
    """Card detail page"""
    model = Card
    template_name = 'pages/card_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cards'] = Card.objects.filter(status='Active')
        context['orders'] = Order.objects.filter(card__pk=self.kwargs['pk'])
        return context

