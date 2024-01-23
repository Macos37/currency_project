from django.urls import path
from .views import CurrencyRateView

urlpatterns = [
    path('get-current-usd/', CurrencyRateView.as_view(), name='get_current_usd'),
]