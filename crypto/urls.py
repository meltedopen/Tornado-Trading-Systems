from django.urls import path
from . import views


# app_name = 'crypto'

urlpatterns = [
    path('', views.crypto_home, name="crypto_home"),
    path('prices/', views.prices, name="prices"),
]
