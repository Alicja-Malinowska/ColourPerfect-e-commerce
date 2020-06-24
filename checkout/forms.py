from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email_address', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country')

    