from django.urls import path
from .views import *

urlpatterns = [
    path('cart-add/<int:pk>', cart_add, name='cart-add'),
    path('cart-remove/<int:pk>', cart_remove, name='cart-remove'),
    path('cart-detail/', cart_detail, name='cart-detail')
]