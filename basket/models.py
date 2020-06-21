from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Basket(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    


class BasketItem(models.Model):
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    colour = models.CharField(max_length=7, null=True,
                              blank=True)
    
