from django.conf import settings
from pizzeria.models import Product


class Cart(object):

    def __init__(self, request):
        self.session = request.session

        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart


    def add(self, book, quantity = 1, update_quantity = False):

        book_id = book.id

        if book_id not in self.cart:
            self.cart[str(book_id)] = {'quantity': 0, 'cost': book.base_cost}

        if update_quantity:
            self.cart[str(book_id)]['quantity'] = quantity
        else:
            self.cart[str(book_id)]['quantity'] += quantity


        self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart



    def remove(self, book):
        book_id = book.id

        if book_id in self.cart:
            self.cart[str(book_id)]['quantity'] -= 1
        ##

        if self.cart[str(book_id)]['quantity'] < 1:
            del self.cart[str(book_id)]
        self.save()


