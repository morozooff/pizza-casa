from .views import *
from django.urls import path, include


urlpatterns = [
    path('create', CreateOrder.as_view(), name='order-create'),
    path('created', CreateOrder.as_view(), name='order-created'),
    path('my-orders/<int:pk>', OrderList.as_view(), name='my-orders'),
    path('order/<int:pk>', OrderDetail.as_view(), name='order-detail')
]