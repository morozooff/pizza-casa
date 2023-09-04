from django.conf import settings
from pizzeria.models import Product


class Cart(object):

    def __init__(self, request):
        self.session = request.session

        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart


    def add(self, product, quantity = 1, update_quantity = False):

        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'cost': product.base_cost}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity


        self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart



    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] -= 1

        if self.cart[product_id]['quantity'] < 1:
            del self.cart[product_id]
        self.save()


    def __iter__(self):

        product_ids = self.cart.keys()
    ##
        products = Product.objects.filter(id__in = product_ids)
    ##
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():

            item['total_cost'] = item['cost'] * item['quantity']

            yield item


    def __len__(self):
        return sum([item['cost'] for item in self.cart.values()])


    def get_total_price(self):
        total_price = 0

        for item in self.cart.values():
            total_price += item['total_cost']

        return total_price

    def clear(self):

        del self.session[settings.CART_SESSION_ID]

        self.session.modified = True
