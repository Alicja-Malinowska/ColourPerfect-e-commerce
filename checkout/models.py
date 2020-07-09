import uuid
from django.db import models
from products.models import Product, Colour
from profiles.models import Profile

# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=240, null=False, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email_address = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=40, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _get_order_number(self):
        
        return uuid.uuid1()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._get_order_number()
        super().save(*args, **kwargs)


    def __str__(self):
        return str(self.order_number)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    colour = models.ForeignKey(Colour, null=True,
                              blank=True, on_delete=models.CASCADE, editable=False)