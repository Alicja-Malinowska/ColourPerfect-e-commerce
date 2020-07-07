from django.test import TestCase
from products.models import Product, Colour, Category, Brand
from basket.models import Basket, BasketItem
from django.contrib.auth import get_user_model

class TestBasketViews(TestCase):

    def setUp(self):

        username = 'testuser'
        password = 'testpass'
        User = get_user_model()
        user = User.objects.create_user(username, password=password)
        Colour.objects.create(hex_value = '#ffffff', name = "colour1", season = "summer")
        Colour.objects.create(hex_value = '#fbced7', name = "colour2", season = "summer")
        category = Category.objects.create(name = "test_category", display_name = "Test Category")
        Brand.objects.create(name = "test_brand", display_name = "Test Brand")
        product = Product.objects.create(brand = Brand.objects.get(name="test_brand"), name = "test_product", price = 5.00, image_link = 'www.test.com', description = "test desc")
        product.category.add(category)

       
        

    def test_get_basket_page(self):

        response = self.client.get("/basket/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "basket.html")
    
    def test_add_product_without_colour(self):
        
        product = Product.objects.get(name = "test_product")
        response = self.client.post(f"/basket/add/{ product.id }", {"redirect_url": f"/products/{ product.id }", "has_colours": "False", "quantity": "1" })
        session = self.client.session
        item_id = str(product.id) + "None"
        self.assertTrue(session['basket'])
        self.assertEqual(session['basket'][item_id]['product'], str(product.id))
        self.assertEqual(session['basket'][item_id]['quantity'], 1)
        self.assertEqual(session['basket'][item_id]['colour'], None)
    
    def test_add_product_as_authenticated_user_no_basket(self):
        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')
        colour1 = Colour.objects.get(name = "colour1")
        colour2 = Colour.objects.get(name = "colour2")
        product = Product.objects.get(name = "test_product")
        product.product_colors.add(colour1, colour2)
        product.save()
        response = self.client.post(f"/basket/add/{ product.id }", {
            "redirect_url": f"/products/{ product.id }", 
            "has_colours": "True", 
            "quantity": "1", 
            "colour": product.product_colors.all()[1]
            })
        basket = Basket.objects.get(owner = user)
        session = self.client.session
        self.assertTrue(BasketItem.objects.filter(basket = basket, product = product, colour = colour2).exists())
        self.assertFalse('basket' in session.keys())

    def test_add_product_as_authenticated_user_existing_basket(self):
        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')
        basket = Basket.objects.create(owner = user)
        colour1 = Colour.objects.get(name = "colour1")
        colour2 = Colour.objects.get(name = "colour2")
        product = Product.objects.get(name = "test_product")
        product.product_colors.add(colour1, colour2)
        product.save()
        response = self.client.post(f"/basket/add/{ product.id }", {
            "redirect_url": f"/products/{ product.id }", 
            "has_colours": "True", 
            "quantity": "1", 
            "colour": product.product_colors.all()[1]
            })
        session = self.client.session
        self.assertTrue(BasketItem.objects.filter(basket = basket, product = product, colour = colour2).exists())
        self.assertFalse('basket' in session.keys())
    
    
    def test_add_product_already_in_basket_as_authenticated_user(self):
        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')
        basket = Basket.objects.create(owner = user)
        product = Product.objects.get(name = "test_product")
        basket_item = BasketItem(basket = basket, product = product, quantity = 1)
        basket_item.save()
        response = self.client.post(f"/basket/add/{ product.id }", {
            "redirect_url": f"/products/{ product.id }", 
            "has_colours": "False", 
            "quantity": "1", 
            })
        added_item = BasketItem.objects.get(id = basket_item.id)
        self.assertEqual(added_item.quantity, 2)

    def test_add_product_already_in_basket_as_not_authenticated_user(self):
        
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
        
        response = self.client.post(f"/basket/add/{ product.id }", {"redirect_url": f"/products/{ product.id }", "has_colours": "False", "quantity": "1" })
        
        self.assertEqual(self.client.session['basket'][item_id]['quantity'], 3)
        

    def test_colour_not_chosen_error(self):

        colour1 = Colour.objects.get(name = "colour1")
        colour2 = Colour.objects.get(name = "colour2")
        product = Product.objects.get(name = "test_product")
        product.product_colors.add(colour1, colour2)
        product.save()

        response = self.client.post(f"/basket/add/{ product.id }", {"redirect_url": f"/products/{ product.id }", "has_colours": "True", "quantity": "1" })
        m = response.cookies.get('messages', '')
        self.assertTrue("Please choose a colour first." in m.output())
    
    def test_adjust_quantity_user_authenticated(self):

        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')
        basket = Basket.objects.create(owner = user)
        product = Product.objects.get(name = "test_product")
        basket_item = BasketItem(basket = basket, product = product, quantity = 1)
        basket_item.save()
        response = self.client.post("/basket/adjust", {"quantity": "2", "item_id": basket_item.id })
        
        self.assertEqual(BasketItem.objects.get(id=basket_item.id).quantity, 2)
    
    def test_adjust_quantity_user_not_authenticated(self):

        product = Product.objects.get(name = "test_product")
        item_id = str(product.id) + "None"
        basket = {}
        basket[item_id] = {
            'product': product.id,
            'quantity': 1,
            'colour': None
        }
        session = self.client.session
        session['basket'] = basket
        session.save()
        
        response = self.client.post("/basket/adjust", {"quantity": "3", "item_id": item_id })
        
        self.assertEqual(self.client.session['basket'][item_id]['quantity'], 3)

    def test_delete_basket_item_user_authenticated(self):
        
        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')
        basket = Basket.objects.create(owner = user)
        product = Product.objects.get(name = "test_product")
        basket_item = BasketItem(basket = basket, product = product, quantity = 1)
        basket_item.save()
        response = self.client.get(f"/basket/delete/{basket_item.id}")
        
        self.assertFalse(BasketItem.objects.filter(id=basket_item.id).exists())

    
    def test_delete_basket_item_user_not_authenticated(self):

        product = Product.objects.get(name = "test_product")
        item_id = str(product.id) + "None"
        basket = {}
        basket[item_id] = {
            'product': product.id,
            'quantity': 1,
            'colour': None
        }
        session = self.client.session
        session['basket'] = basket
        session.save()
        
        response = self.client.get(f"/basket/delete/{item_id}")
        
        self.assertFalse(item_id in self.client.session['basket'].keys())
    
    def test_raise_404_if_basket_item_being_deleted_does_not_exists_user_auth(self):

        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')
        response = self.client.get("/basket/delete/0")
        
        self.assertEqual(response.status_code, 404)

    def test_raise_404_if_basket_item_being_deleted_does_not_exists_user_not_auth(self):

        response = self.client.get("/basket/delete/0")
        
        self.assertEqual(response.status_code, 404)
        
    