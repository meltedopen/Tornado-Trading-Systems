from django.shortcuts import render

# Create your views here.


def crypto_home(request):
    import requests
    import json

    # Grab Crypto Price Data
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,EOS,LTC,BCH,XRP,ETC,TRX,ZEC,QTUM&tsyms=USD")
    price = json.loads(price_request.content)

    # Grab Crypto News
    api_request = requests.get(
        "https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'crypto/crypto_home.html', {'api': api, 'price': price})


def prices(request):
    return render(request, 'crypto/prices.html', {})
