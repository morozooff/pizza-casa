from django import forms

PRODUCTS_VALUE_CHOICES = [1, 2, 3, 4, 5]


class AddToCartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCTS_VALUE_CHOICES, coerce=int, label='Quantity')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
