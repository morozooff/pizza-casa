from django import forms

PRODUCTS_VALUE_CHOICES = [(i, str(i)) for i in range(1, 20)]


class AddToCartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCTS_VALUE_CHOICES, coerce=int, label='Quantity')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
