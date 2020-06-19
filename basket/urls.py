from django.urls import path
from basket.views import basket

urlpatterns = [
    path('', basket, name='basket'),
]