from django.db import models

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Colour(models.Model):
    hex_value = models.CharField(max_length=7)
    name = models.CharField(max_length=254, null=True, blank=True)
    season = models.CharField(max_length=10)

    def __str__(self):
        return self.hex_value

class Brand(models.Model):
    name = models.CharField(max_length=254, null=True)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name

class Product(models.Model):
    brand = models.ManyToManyField(Brand)
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    image_link = models.URLField(max_length=1024, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ManyToManyField(Category)
    product_colors = models.ManyToManyField(Colour)


    def __str__(self):
        return self.name

    