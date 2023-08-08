from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.reverse import reverse
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from .forms import AddToCartForm
from .cart import Cart
from pizzeria.models import Product


@api_view()
def cart_add(request: Request, product_id: int) -> HttpResponseRedirect:
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartForm(request.data)

    if form.is_valid():
        form_data = form.cleaned_data
        cart.add(product=product, quantity=form_data.get(['quantity']), update_quantity=form_data.get(['update']))

    return HttpResponseRedirect(redirect_to=reverse('cart-detail'))


@api_view()
def cart_remove(request: Request, product_id: int) -> HttpResponseRedirect:
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.remove(product)

    return HttpResponseRedirect(redirect_to=reverse('cart-detail'))


@api_view()
@renderer_classes([TemplateHTMLRenderer])
@permission_classes([IsAuthenticated])
def cart_detail(request: Request) -> Response:
    cart = Cart(request)

    return Response({'cart': cart}, template_name='cart/cart-detail.html')

