from django import forms
from localflavor.ca.forms import CAPostalCodeField
from .models import Order


class OrderCreateForm(forms.ModelForm):
    postal_code = CAPostalCodeField()
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']
