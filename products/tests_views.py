from django.test import TestCase
from products.models import Product, Colour, Category, Brand
from wishlist.models import Wishlist, WishlistItem
from django.contrib.auth import get_user_model

# Create your tests here.

class TestProductsViews(TestCase):

    def setUp(self):

        username = 'testuser'
        password = 'testpass'
        User = get_user_model()
        user = User.objects.create_user(username, password=password)
        c1 = Colour.objects.create(hex_value = '#ffffff', name = "summer_colour", season = "summer")
        c2 = Colour.objects.create(hex_value = '#fbced7', name = "spring_colour", season = "spring")
        c3 = Colour.objects.create(hex_value = '#bbbbbb', name = "winter_colour", season = "winter")
        c4 = Colour.objects.create(hex_value = '#ff0000', name = "autumn_colour", season = "autumn")
        c5 = Colour.objects.create(hex_value = '#fff000', name = "autumn_colour", season = "autumn")
        category = Category.objects.create(name = "test_category", display_name = "Test Category")
        brand = Brand.objects.create(name = "test_brand", display_name = "Test Brand")
        product = Product.objects.create(brand = brand, name = "test_product", price = 5.00, image_link = 'www.test.com', description = "test desc")
        product.category.add(category)
        product.product_colors.add(c1, c2, c3, c4, c5)
        wishlist_product = Product.objects.create(brand = brand, name = "wishlist_product", price = 5.00, image_link = 'www.test.com', description = "wishlist desc")
        wishlist_product.category.add(category)
        wishlist_product.product_colors.add(c1, c5)
        wishlist = Wishlist.objects.create(owner = user)
        WishlistItem.objects.create(wishlist = wishlist, product = wishlist_product, colour = c5)
    
    def test_get_product_page(self):

        product = Product.objects.get(name = "test_product")
        response = self.client.get(f"/products/{ product.id }")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "product.html")
    
    def test_product_colours_sorted_accroding_to_seasons(self):

        product = Product.objects.get(name = "test_product")
        response = self.client.get(f"/products/{ product.id }")

        self.assertEqual(len(response.context['colours']), 4)
        self.assertEqual(len(response.context['colours']['Spring']), 1)
        self.assertEqual(len(response.context['colours']['Autumn']), 2)
        self.assertEqual(response.context['colours']['Winter'][0].name, "winter_colour")
    
    def test_get_search_page(self):

        response = self.client.get("/products/category/test_category")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search.html")
    

    def test_get_products_by_category(self):

        category = Category.objects.get(name = "test_category")

        response = self.client.get(f"/products/category/{ category.name }")

        self.assertEqual(len(response.context['products']), 2)
        self.assertEqual(response.context['products'][0][0].name, "test_product")

    

    def test_category_doesnt_exist(self):

        response = self.client.get(f"/products/category/doesnt-exist")

        self.assertEqual(response.context['searched'], "none")
        self.assertTrue("This category does not exist." in response.content.decode())


    def test_get_products_by_brand(self):

        brand = Brand.objects.get(name = "test_brand")

        response = self.client.get(f"/products/brand/{ brand.name }")

        self.assertEqual(len(response.context['products']), 2)
        self.assertEqual(response.context['products'][0][0].name, "test_product")

    

    def test_brand_doesnt_exist(self):

        response = self.client.get(f"/products/brand/doesnt-exist")

        self.assertEqual(response.context['searched'], "none")
        self.assertTrue("sell this" in response.content.decode())


    def test_get_products_matching_search_phrase(self):


        response = self.client.get(f"/products/search/ ", { 'phrase': 'wishlist' })

        self.assertEqual(len(response.context['products']), 1)
        self.assertEqual(response.context['products'][0][0].description, "wishlist desc")


    def test_search_phrase_empty(self):

        response = self.client.get(f"/products/search/ ", { 'phrase': '' })

        m = response.cookies.get('messages', '')
        self.assertTrue("Please type a phrase you want to search for" in m.output())
    
    def test_mark_items_on_wishlist(self):

        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')

        response = self.client.get(f"/products/search/ ", { 'phrase': 'product' })

        self.assertEqual(response.context['products'][0][0].name, "test_product")
        self.assertFalse(response.context['products'][0][1])
        self.assertEqual(response.context['products'][1][0].name, "wishlist_product")
        self.assertTrue(response.context['products'][1][1])











