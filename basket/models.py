from django.db import models
from products.models import Product, Colour
from django.contrib.auth.models import User

# Create your models here.


class Basket(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    


class BasketItem(models.Model):
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    colour = models.ForeignKey(Colour, null=True,
                              blank=True, on_delete=models.CASCADE, editable=False)
    
