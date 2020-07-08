from django.test import TestCase
from products.models import Product, Colour, Category, Brand

# Create your tests here.

class TestProductsModels(TestCase):

    def test_product_created_correctly(self):

        c1 = Colour.objects.create(hex_value = '#ffffff', name = "colour1", season = "summer")
        c2 = Colour.objects.create(hex_value = '#fbced7', name = "colour2", season = "summer")
        category = Category.objects.create(name = "test_category", display_name = "Test Category")
        brand = Brand.objects.create(name = "test_brand", display_name = "Test Brand")
        product = Product.objects.create(brand = brand, name = "test_product", price = 5.00, image_link = 'www.test.com', description = "test desc")
        product.category.add(category)
        product.product_colors.add(c1, c2)

        self.assertEqual(product.product_colors.all()[0].hex_value, "#ffffff")
        self.assertEqual(product.category.all()[0].name, "test_category")
        self.assertEqual(product.brand.name, "test_brand")
    
    def test_category_method_returns_display_name(self):

        category = Category.objects.create(name = "test_category", display_name = "Test Category")

        self.assertEqual(category.get_display_name(), "Test Category")
    

    def test_brand_method_returns_display_name(self):

        brand = Brand.objects.create(name = "test_brand", display_name = "Test Brand")

        self.assertEqual(brand.get_display_name(), "Test Brand")
        

