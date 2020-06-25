from django.db import models
from products.models import Product, Colour
from django.contrib.auth.models import User

# Create your models here.


class Wishlist(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    


class WishlistItem(models.Model):
    wishlist = models.ForeignKey('Wishlist', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    colour = models.ForeignKey(Colour, null=True,
                              blank=True, on_delete=models.CASCADE, editable=False)
    
