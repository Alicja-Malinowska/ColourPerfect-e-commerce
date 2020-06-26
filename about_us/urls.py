from django.urls import path
from about_us.views import about_us, delivery_returns


urlpatterns = [
    path('', about_us, name='about_us'),
    path('delivery', delivery_returns, name='delivery_returns'),


]