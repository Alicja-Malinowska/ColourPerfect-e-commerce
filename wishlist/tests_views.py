from django.test import TestCase
from django.contrib.auth import get_user_model
from django.http import Http404
from wishlist.models import Wishlist, WishlistItem
from products.models import Product, Colour, Category, Brand


class TestProfilesViews(TestCase):

    def setUp(self):
        username = 'testuser'
        password = 'testpass'
        User = get_user_model()
        user = User.objects.create_user(username, password=password)
        c1 = Colour.objects.create(hex_value = '#ffffff', name = "colour1", season = "summer")
        c2 = Colour.objects.create(hex_value = '#fbced7', name = "colour2", season = "summer")
        category = Category.objects.create(name = "test_category", display_name = "Test Category")
        brand = Brand.objects.create(name = "test_brand", display_name = "Test Brand")
        product = Product.objects.create(brand = brand, name = "test_product", price = 5.00, image_link = 'www.test.com', description = "test desc")
        product.category.add(category)
        product.product_colors.add(c1, c2)
        wishlist = Wishlist.objects.create(owner = user)
        WishlistItem.objects.create(wishlist = wishlist, product = product, colour = product.product_colors.all()[0])



    def test_redirect_to_login_page_if_not_authenticated_user(self):

        response = self.client.get("/wishlist/")

        self.assertRedirects(response, '/accounts/login/?next=/wishlist/')
    

    def test_get_wishlist_page(self):

        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')

        response = self.client.get("/wishlist/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "wishlist.html")
    
    def test_add_new_wishlist_item(self):

        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')

        product = Product.objects.get(name = "test_product")
        colour = Colour.objects.get(name = "colour2")

        response = self.client.post(f"/wishlist/add/{ product.id }", {"redirect_url": f"/products/{ product.id }", "colour": colour.hex_value})

        self.assertTrue(WishlistItem.objects.filter(colour = colour))

    def test_add_existing_item(self):

        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')

        product = Product.objects.get(name = "test_product")

        existing_item = WishlistItem.objects.get(colour = product.product_colors.all()[0])

        response = self.client.post(f"/wishlist/add/{ product.id }", {"redirect_url": f"/products/{ product.id }", "colour": product.product_colors.all()[0]})

        m = response.cookies.get('messages', '')
        self.assertTrue("already on your wishlist" in m.output())

    def test_delete_item(self):

        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')

        wishlist = Wishlist.objects.get(owner = user)
        item = WishlistItem.objects.get(wishlist = wishlist)

        response = self.client.get(f"/wishlist/delete/{ item.id }")

        self.assertFalse(WishlistItem.objects.filter(wishlist = wishlist).exists())
        self.assertTrue(Wishlist.objects.filter(owner = user).exists())
    
    def test_delete_non_existent_item(self):

        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')

        response = self.client.get(f"/wishlist/delete/0")

        self.assertRaises(Http404)


    
