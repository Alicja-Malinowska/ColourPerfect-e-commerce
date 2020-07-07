from django.test import TestCase
from checkout.models import Order, OrderItem
from products.models import Product, Colour, Category, Brand
from basket.models import Basket, BasketItem
from profiles.models import Profile
from django.contrib.auth import get_user_model


# Create your tests here.

class TestCheckoutViews(TestCase):

    def setUp(self):

        order = Order.objects.create(
            first_name = 'test name',
            last_name = 'test last name',
            email_address = 'test@gmail.com',
            phone_number = '123 456 789',
            street_address1 = 'test street 1',
            street_address2 = '',
            town_or_city = 'test city',
            postcode = '',
            country = 'test country')

        colour = Colour.objects.create(hex_value = '#fbced7', name = "colour2", season = "summer")
        cat = Category.objects.create(name = "test_category", display_name = "Test Category")
        Brand.objects.create(name = "test_brand", display_name = "Test Brand")
        product = Product.objects.create(brand = Brand.objects.get(name="test_brand"), name = "test_product", price = 5.00, image_link = 'www.test.com', description = "test desc")
        product.category.add(cat)

        OrderItem.objects.create(order = order, product = product, quantity = 3, colour = colour)
        username = 'testuser'
        password = 'testpass'
        User = get_user_model()
        user = User.objects.create_user(username, password=password)
        basket = Basket.objects.create(owner = user)
        BasketItem.objects.create(basket = basket, product = product, quantity = 1)


    def test_get_checkout_page(self):

        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')
    
        basket = Basket.objects.get(owner = user)

        response = self.client.get("/checkout/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout.html")
        self.assertTrue(response.context['stripe_public_key'])
        self.assertTrue(response.context['client_secret'])
    

    def test_get_checkout_success_page(self):

        order = Order.objects.get(first_name = 'test name')
        response = self.client.get(f"/checkout/success/{order.order_number}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout-success.html")
    

    def test_display_error_message_if_form_is_not_valid(self):

        response = self.client.post("/checkout/", {
            'first_name': '',
            'last_name': 'test last name',
            'email_address': 'test@gmail.com',
            'phone_number': '123 456 789',
            'street_address1': 'test street 1',
            'street_address2': '',
            'town_or_city': 'test city',
            'postcode': '',
            'country': 'test country'
            })
        
        m = response.cookies.get('messages', '')
        self.assertTrue("There is an error in your form" in m.output())
        



    def test_stay_in_basket_view_if_basket_empty(self):

        response = self.client.get("/checkout/")
        self.assertRedirects(response, "/basket/")
    
    def test_stay_in_basket_view_if_basket_empty_user_authenticated(self):

        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')
        basket = BasketItem.objects.filter(basket__owner=user)
        basket.delete()
        response = self.client.get("/checkout/")
        
        self.assertRedirects(response, "/basket/")

    def test_total_saved_in_created_order(self):

        product = Product.objects.get(name = "test_product")
        item_id = str(product.id) + "1"
        colour = Colour.objects.get(hex_value = '#fbced7')
        basket = {}
        basket[item_id] = {
            'product': product.id,
            'quantity': 2,
            'colour': colour.id
        }
        session = self.client.session
        session['basket'] = basket
        session.save()

        response = self.client.post("/checkout/", {
            'first_name': 'other test name',
            'last_name': 'test last name',
            'email_address': 'test@gmail.com',
            'phone_number': '123 456 789',
            'street_address1': 'test street 1',
            'street_address2': '',
            'town_or_city': 'test city',
            'postcode': '',
            'country': 'test country'})
        
       
        order = Order.objects.get(first_name = 'other test name')
        expected_total = product.price * basket[item_id]['quantity']
        self.assertEqual(order.total, expected_total)
    
    def test_save_delivery_details_in_profile(self):

        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')

        basket = Basket.objects.get(owner = user)

        response = self.client.post("/checkout/", {
            'first_name': 'other test name',
            'last_name': 'test last name',
            'email_address': 'othertest@gmail.com',
            'phone_number': '123 456 789',
            'street_address1': 'test street 1',
            'street_address2': '',
            'town_or_city': 'test city',
            'postcode': '',
            'country': 'test country',
            'save': 'on'})
        
        profile =  Profile.objects.get(first_name = 'other test name')
        self.assertEqual(profile.email_address, 'othertest@gmail.com')
    

    def test_profile_saved_in_order(self):

        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')

        order = Order.objects.get(first_name = 'test name')
        
        response = response = self.client.get(f"/checkout/success/{order.order_number}")
        

        self.assertEqual(Order.objects.get(first_name = 'test name').profile, Profile.objects.get(owner=user))
    
    
    def test_all_basket_items_deleted_on_checkout_success_authorised_user(self):

        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')

        order = Order.objects.get(first_name = 'test name')
        basket = Basket.objects.get(owner = user)

        response = response = self.client.get(f"/checkout/success/{order.order_number}")

        self.assertFalse(BasketItem.objects.filter(basket__owner = user).exists())


    def test_session_basket_deleted_on_checkout_success_not_authorised_user(self):

        product = Product.objects.get(name = "test_product")
        item_id = str(product.id) + "None"
        basket = {}
        basket[item_id] = {
            'product': product.id,
            'quantity': 2,
            'colour': None
        }
        session = self.client.session
        session['basket'] = basket
        session.save()

        order = Order.objects.get(first_name = 'test name')

        response = response = self.client.get(f"/checkout/success/{order.order_number}")

        self.assertFalse('basket' in self.client.session.keys())
        
