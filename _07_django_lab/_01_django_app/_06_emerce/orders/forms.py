from django import forms
from .models import Order

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'address_lane_1', 'address_lane_2', 'country', 'state', 'city', 'order_note']
