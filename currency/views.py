from django.http import JsonResponse
from django.views import View
from .models import Currency
import requests
from .utils import pause_between_requests


class CurrencyRateView(View):
    def get_data_currency(self):
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()
        return data['rates']['RUB']

    @pause_between_requests
    def get(self, request):
        data_rate = self.get_data_currency()
        Currency.objects.create(usd_to_rub_rate=data_rate)
        history_rate = Currency.objects.order_by('-timestamp')[:10]
        request_history = [
            {'timestamp': history.timestamp,
                'usd_to_rub_rate': history.usd_to_rub_rate}
            for history in history_rate
            ]
        return JsonResponse({'data': data_rate, 'history': request_history})

