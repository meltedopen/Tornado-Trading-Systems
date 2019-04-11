from django.shortcuts import render
import requests
import json
# Create your views here.


def crypto_home(request):

    # Grab Crypto Price Data
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,EOS,LTC,BCH,XRP,ETC,TRX,ZEC,QTUM&tsyms=USD&api_key=adc24715bb4b41bc5cdc1690da7f8804f3c0127527cfe0d335716323ecba00a6")
    price = json.loads(price_request.content)

    # Grab Crypto News
    api_request = requests.get(
        "https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key=adc24715bb4b41bc5cdc1690da7f8804f3c0127527cfe0d335716323ecba00a6", )
    api = json.loads(api_request.content)
    return render(request, 'crypto/crypto_home.html', {'api': api, 'price': price})

# params={"sortOrder": "popular"}


def crypto_prices(request):
    if request.method == 'POST':
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD&api_key=adc24715bb4b41bc5cdc1690da7f8804f3c0127527cfe0d335716323ecba00a6")
        crypto = json.loads(crypto_request.content)
        return render(request, 'crypto/crypto_prices.html', {'quote': quote, 'crypto': crypto})

    else:
        notfound = "Enter a crypto currency symbol into the form above..."
        return render(request, 'crypto/crypto_prices.html', {'notfound': notfound})
