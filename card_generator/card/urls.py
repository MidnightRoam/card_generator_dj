from django.urls import path

from .views import IndexView, GenerateCardView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('generator', GenerateCardView.as_view(), name='generator'),
]
