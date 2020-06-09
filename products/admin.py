from django.contrib import admin
from products.models import Colour, Product, Category, Brand
# Register your models here.


admin.site.register(Colour)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)