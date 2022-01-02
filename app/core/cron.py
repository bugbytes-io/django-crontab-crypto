from django.conf import settings
import requests
from core.models import Crypto, CryptoPrice


def fetch_crypto_prices():
    headers = {
        "X-CMC_PRO_API_KEY": settings.CMC_API_KEY
    }

    resp = requests.get(settings.API_URL, headers=headers)

    data = resp.json()['data']

    for currency in data:
        name = currency['name']
        symbol = currency['symbol']
        price = currency['quote']['USD']['price']

        print(name, symbol, price)

        # get_or_create the Crypto object
        crypto = Crypto.objects.get_or_create(name=name, symbol=symbol)[0]

        # now add the latest crypto price
        CryptoPrice.objects.create(crypto=crypto, price=price)