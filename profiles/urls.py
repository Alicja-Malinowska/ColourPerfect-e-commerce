from django.urls import path
from profiles.views import profile, order_history

urlpatterns = [
    path('', profile, name='profile'),
    path('order-history', order_history, name='order_history')

]