from django.urls import path
from . import views


# app_name = 'crypto'

urlpatterns = [
    path('crypto/', views.crypto_home, name="crypto_home"),
    path('prices/', views.crypto_prices, name="crypto_prices"),
]
