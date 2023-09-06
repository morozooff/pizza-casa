from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from pizzeria.models import Product

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250, default='Moscow, Pizzeria Pizza-Casa')
    created = models.DateTimeField(default=datetime.now())

    PLACE_OF_ISSUE_CHOICES = (('IP', 'In Pizzeria'),
                              ('DYA', 'Delivery on Your Own Address'))

    place_of_issue = models.CharField(max_length=100, choices =PLACE_OF_ISSUE_CHOICES, default='IP')

    class Meta:
        ordering = ['-created', ]
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


    def __str__(self):
        return f'Order №{self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    cost = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.cost * self.quantity
