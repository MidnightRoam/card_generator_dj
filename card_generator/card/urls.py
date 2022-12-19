from django.urls import path

from .views import IndexView, GenerateCardView, CardDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('card-generator/', GenerateCardView.as_view(), name='generator'),
    path('<int:pk>/', CardDetailView.as_view(), name='profile')
]
