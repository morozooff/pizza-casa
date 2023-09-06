from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib import messages
from rest_framework.renderers import TemplateHTMLRenderer
from .forms import OrderCreateForm
from cart.cart import Cart
from .models import OrderItem, Order
from rest_framework import generics
from users.models import Profile

class CreateOrder(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        cart = Cart(request)
        form = OrderCreateForm()
        return Response({'form': form, 'cart': cart}, template_name='orders/create.html')

    def post(self, request):
        cart = Cart(request)
        form = OrderCreateForm(request.data)

        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user

            place_of_issue = form.cleaned_data.get('place_of_issue')
            if place_of_issue == 'DYA':
                profile = get_object_or_404(Profile, user = request.user)
                order.address = profile.address

            order.save()

            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         cost=item['cost'],
                                         quantity=item['quantity'])
            cart.clear()

            return Response({'form': form, 'cart': cart, 'order': order}, template_name='orders/created.html')


class OrderList(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        user = request.user
        user_orders = Order.objects.filter(customer = user)

        return Response({'user_orders': user_orders}, template_name='orders/user_orders.html')


class OrderDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, pk):

        order = get_object_or_404(Order, id=pk)
        return Response({'order': order}, template_name='orders/order_detail.html')







