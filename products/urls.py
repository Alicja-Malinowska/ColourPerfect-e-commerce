from django.urls import path
from products.views import product

urlpatterns = [
    path('<id>', product, name='product')
]