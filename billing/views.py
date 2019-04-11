from django.shortcuts import render

# Create your views here.

import stripe
stripe.api_key = "sk_test_0QLbislljyzSwIi7KZpv48nM00mPgwBWWL"


STRIPE_PUB_KEY = 'pk_test_XKY9gcsPWw4GacnkoErk4FMo00E6FkTSdB'


def payment_method_view(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY})
