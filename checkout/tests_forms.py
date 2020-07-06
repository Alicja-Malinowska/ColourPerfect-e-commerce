from django.test import TestCase
from checkout.forms import OrderForm

# Create your tests here.

class TestOrderForm(TestCase):

    def test_create_order_with_mandatory_fields_filled(self):
        form = OrderForm({
            'first_name': 'test', 
            'last_name': 'test', 
            'email_address': 'test@gmail.com', 
            'phone_number' : '123 456 789',
            'street_address1' : '5 test street',
            'town_or_city' : 'test city', 
            'country': 'test country'})

        self.assertTrue(form.is_valid())
    
    def test_correct_message_for_empty_form(self):
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['first_name'], [u'This field is required.'])