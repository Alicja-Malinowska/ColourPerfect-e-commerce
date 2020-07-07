from django.test import TestCase
from products.models import Product, Colour, Category, Brand

# Create your tests here.

class TestHomeViews(TestCase):

    def setUp(self):

        c1 = Colour.objects.create(hex_value = '#ffffff', name = "summer_colour", season = "summer")
        c2 = Colour.objects.create(hex_value = '#fbced7', name = "spring_colour", season = "spring")
        c3 = Colour.objects.create(hex_value = '#bbbbbb', name = "winter_colour", season = "winter")
        c4 = Colour.objects.create(hex_value = '#ff0000', name = "autumn_colour", season = "autumn")
        category = Category.objects.create(name = "test_category", display_name = "Test Category")
        Brand.objects.create(name = "test_brand", display_name = "Test Brand")
        product_1 = Product.objects.create(brand = Brand.objects.get(name="test_brand"), name = "test_product1", price = 5.00, image_link = 'www.test.com', description = "test desc")
        product_1.category.add(category)
        product_1.product_colors.add(c1, c2, c3, c4)
        
        product_2 = Product.objects.create(brand = Brand.objects.get(name="test_brand"), name = "test_product2", price = 15.00, image_link = 'www.test.com', description = "test desc")
        product_2.category.add(category)
        product_2.product_colors.add(c1, c2, c3, c4)

        product_3 = Product.objects.create(brand = Brand.objects.get(name="test_brand"), name = "test_product3", price = 25.00, image_link = 'www.test.com', description = "test desc")
        product_3.category.add(category)
        product_3.product_colors.add(c1, c2, c3, c4)

        

    def test_get_home_page(self):

        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
    
    def test_get_suggestions_for_each_season(self):

        response = self.client.get("/")

        self.assertEqual(len(response.context['suggestions']), 4)
        self.assertEqual(len(response.context['suggestions']['Spring']), 3)
        self.assertEqual(response.context['suggestions']['Spring'][0][1].name, "spring_colour")
        self.assertEqual(len(response.context['suggestions']['Winter']), 3)
        self.assertEqual(response.context['suggestions']['Winter'][0][1].name, "winter_colour")
        self.assertNotEqual(response.context['suggestions']['Autumn'][0][1].name, "summer_colour")
        

