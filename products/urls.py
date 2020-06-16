from django.urls import path
from products.views import product, search

urlpatterns = [
    path('<q_type>/<query>', search, name="search" ),
    path('<id>', product, name='product'),
    
]