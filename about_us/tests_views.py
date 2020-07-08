from django.test import TestCase

# Create your tests here.
class TestAboutUsViews(TestCase):

    def test_get_about_page(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about-us.html")
    
    def test_get_delivery_section(self):
        response = self.client.get("/about/delivery")
        self.assertRedirects(response, "/about/#delivery-returns")
    
