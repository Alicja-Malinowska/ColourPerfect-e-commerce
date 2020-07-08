from django.test import TestCase
from django.contrib.auth import get_user_model
from profiles.models import Profile


class TestProfilesViews(TestCase):

    def setUp(self):
        username = 'testuser'
        password = 'testpass'
        User = get_user_model()
        user = User.objects.create_user(username, password=password)


    def test_redirect_to_login_page_if_not_authenticated_user(self):

        response = self.client.get("/profile/")

        self.assertRedirects(response, '/accounts/login/?next=/profile/')
    

    def test_get_profile_page(self):

        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')

        response = self.client.get("/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profile.html")
    

    def test_update_details(self):

        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')

        profile = Profile.objects.get(owner = user)

        response = self.client.post("/profile/", {
            'first_name': 'profile test name',
            'last_name': 'profile last name',
            'email_address': 'test@gmail.com',
            'phone_number': '123 456 789',
            'street_address1': 'test street 1',
            'street_address2': '',
            'town_or_city': 'test city',
            'postcode': '',
            'country': 'test country'})
        
        updated_profile = Profile.objects.get(owner = user)

        self.assertEqual(profile.first_name, '')
        self.assertEqual(updated_profile.first_name, 'profile test name')
    

    def test_get_order_history(self):

        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')

        response = self.client.get("/profile/order-history")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "order-history.html")
        self.assertTrue('orders' in response.context)
    
    
    def test_display_error_message_if_profile_form_is_not_valid(self):

        User = get_user_model()
        user = User.objects.get(username='testuser')
        logged_in = self.client.login(username='testuser', password='testpass')

        response = self.client.post("/profile/", {
            'first_name': 'profile test name',
            'last_name': 'profile last name',
            'email_address': 'test',
            'phone_number': '123 456 789',
            'street_address1': 'test street 1',
            'street_address2': '',
            'town_or_city': 'test city',
            'postcode': '',
            'country': 'test country'})
        
        m = response.cookies.get('messages', '')
        self.assertTrue("An error occured" in m.output())




