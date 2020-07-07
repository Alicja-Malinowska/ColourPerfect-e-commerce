import re
from django.test import TestCase
from checkout.models import Order, OrderItem
from products.models import Product, Colour, Category, Brand
from datetime import datetime

# Create your tests here.

class TestCheckoutModels(TestCase):
    

    def test_create_correct_order_object(self):
        
        order = Order(
            first_name = 'test name',
            last_name = 'test last name',
            email_address = 'test@gmail.com',
            phone_number = '123 456 789',
            street_address1 = 'test street 1',
            street_address2 = '',
            town_or_city = 'test city',
            postcode = '',
            country = 'test country')

        order.save()
        assert re.match(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$', str(order.order_number))
        self.assertEqual(order.date.day, datetime.now().day)
        self.assertEqual(order.total, 0)

    def test_order_string_method_returns_order_number(self):

        order = Order(
            first_name = 'test name',
            last_name = 'test last name',
            email_address = 'test@gmail.com',
            phone_number = '123 456 789',
            street_address1 = 'test street 1',
            street_address2 = '',
            town_or_city = 'test city',
            postcode = '',
            country = 'test country')

        order.save()

        self.assertEqual(str(order), str(order.order_number))

    def test_create_correct_order_item(self):

       
        colour = Colour.objects.create(hex_value = '#fbced7', name = "colour2", season = "summer")
        cat = Category.objects.create(name = "test_category", display_name = "Test Category")
        Brand.objects.create(name = "test_brand", display_name = "Test Brand")
        product = Product.objects.create(brand = Brand.objects.get(name="test_brand"), name = "test_product", price = 5.00, image_link = 'www.test.com', description = "test desc")
        product.category.add(cat)
       

        order = Order(
            first_name = 'test name',
            last_name = 'test last name',
            email_address = 'test@gmail.com',
            phone_number = '123 456 789',
            street_address1 = 'test street 1',
            street_address2 = '',
            town_or_city = 'test city',
            postcode = '',
            country = 'test country')

        order.save()

        item = OrderItem(order = order, product = product, quantity = 3, colour = colour)

        self.assertEqual(item.order.first_name, 'test name')
        self.assertEqual(item.product.category.all()[0].name, 'test_category')
        self.assertEqual(item.colour.hex_value, '#fbced7')

    