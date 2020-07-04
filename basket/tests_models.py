from django.test import TestCase
from basket.models import Basket, BasketItem
from products.models import Product, Colour, Category, Brand
from django.contrib.auth import get_user_model


# Create your tests here.
class TestBasketItemModel(TestCase):
    def test_basket_item_deleted_when_basket_deleted(self):
        user = get_user_model().objects.create_user(username='testuser', email='test@testing.com', password='password')
        basket = Basket(owner = user)
        basket.save()
        colour = Colour(hex_value = '#ffffff', name = "white", season = "summer")
        colour.save()
        category = Category(name = "test_category", display_name = "Test Category")
        category.save()
        brand = Brand(name = "test_brand", display_name = "Test Brand")
        brand.save()
        product = Product(brand = brand, name = "test name", price = 5.00, image_link = 'www.test.com', description = "test desc")
        product.save()
        product.category.add(category)
        product.product_colors.add(colour)
        item = BasketItem(basket = basket, product = product, quantity = 1, colour = colour)
        item.save()
        basket.delete()
        self.assertFalse(BasketItem.objects.filter(basket = basket).exists())

        
