from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['place_of_issue']
        labels = {'place_of_issue': 'Choice place, where you may pick your order'}
