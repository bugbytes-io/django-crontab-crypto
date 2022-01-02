from django.http.response import HttpResponse
from django.shortcuts import render
from core.models import Crypto, CryptoPrice

def index(request):
    bitcoin = Crypto.objects.get(name='Bitcoin')
    prices = CryptoPrice.objects.filter(crypto=bitcoin)

    context = {'currency': bitcoin, 'crypto_prices': prices}
    if request.htmx:
        return HttpResponse(''.join([f'<li>{p.price}</li>' for p in prices]))
    return render(request, 'index.html', context)