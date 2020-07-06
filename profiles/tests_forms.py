from django.test import TestCase
from django.contrib.auth import get_user_model
from profiles.forms import ProfileForm

# Create your tests here.

class TestProfilesForms(TestCase):

    def test_create_profile_form_with_mandatory_fields_filled(self):
        form = ProfileForm({
            'first_name': 'test', 
            'last_name': 'test', 
            'email_address': 'test@gmail.com', 
            'phone_number' : '123 456 789',
            'street_address1' : '5 test street',
            'town_or_city' : 'test city', 
            'country': 'test country'})

        self.assertTrue(form.is_valid())
    
    def test_correct_message_for_empty_form(self):
        form = ProfileForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['first_name'], [u'This field is required.'])


