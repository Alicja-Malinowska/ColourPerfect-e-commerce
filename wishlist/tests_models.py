from django.test import TestCase
from django.contrib.auth import get_user_model
from wishlist.models import Wishlist, WishlistItem
from products.models import Product, Category, Colour, Brand

# Create your tests here.

class TestWishlistModels(TestCase):

    def setUp(self):

        c1 = Colour.objects.create(hex_value = '#ffffff', name = "colour1", season = "summer")
        c2 = Colour.objects.create(hex_value = '#fbced7', name = "colour2", season = "summer")
        category = Category.objects.create(name = "test_category", display_name = "Test Category")
        brand = Brand.objects.create(name = "test_brand", display_name = "Test Brand")
        product = Product.objects.create(brand = brand, name = "test_product", price = 5.00, image_link = 'www.test.com', description = "test desc")
        product.category.add(category)
        product.product_colors.add(c1, c2)
        username = 'testuser'
        password = 'testpass'
        User = get_user_model()
        user = User.objects.create_user(username, password=password)
        Wishlist.objects.create(owner = user)



    def test_wishlist_item_created_correctly(self):
        
        User = get_user_model()
        user = User.objects.get(username='testuser')
        wishlist = Wishlist.objects.get(owner = user)
        product = Product.objects.get(name = "test_product")
        wishlist_item = WishlistItem(wishlist = wishlist, product = product, colour = product.product_colors.all()[0])

        self.assertEqual(wishlist_item.wishlist.owner, user)
        self.assertEqual(wishlist_item.product.name, product.name)
        self.assertEqual(wishlist_item.colour, product.product_colors.all()[0])
        self.assertEqual(product.product_colors.all()[0].name, 'colour1')
        self.assertEqual(wishlist_item.colour.name, 'colour1')
    
    def test_wishlist_item_deleted_when_wishlist_deleted(self):

        User = get_user_model()
        user = User.objects.get(username='testuser')
        wishlist = Wishlist.objects.get(owner = user)
        product = Product.objects.get(name = "test_product")
        wishlist_item = WishlistItem(wishlist = wishlist, product = product, colour = product.product_colors.all()[0])

        wishlist.delete()

        self.assertFalse(WishlistItem.objects.filter(wishlist__owner = user).exists())




