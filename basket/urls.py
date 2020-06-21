from django.urls import path
from basket.views import basket, add_to_basket

urlpatterns = [
    path('', basket, name='basket'),
    path('add/<product_id>', add_to_basket, name='add_to_basket'),

]