from django.test import TestCase
from django.contrib.auth import get_user_model
from profiles.models import Profile

# Create your tests here.

class TestProfilesModels(TestCase):

    def test_create_profile_on_user_creation(self):

        username = 'testuser'
        password = 'testpass'
        User = get_user_model()
        user = User.objects.create_user(username, password=password)

        self.assertTrue(Profile.objects.filter(owner = user).exists())