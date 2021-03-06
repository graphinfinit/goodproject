from .models import Cart, Order
from django.forms import ModelForm, HiddenInput

from django import forms

class CartForm(ModelForm):
    number = forms.IntegerField(min_value=1)
    class Meta:
        model = Cart
        fields = ('session_key', 'product', 'number')
        widgets = {'session_key': HiddenInput(), 'product': HiddenInput()}
        labels = {'number': ''}
        help_texts = {'number': ''}


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['phone', 'email', 'adress_dostavka', 'comment']

        required_css_class = "field"
