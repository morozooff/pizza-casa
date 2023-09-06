from django.contrib import admin
from .models import *
from django.contrib.admin.decorators import register


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_in_fields = ['product']


@register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'address', 'place_of_issue', 'created']
    inlines = [
        OrderItemInline,
    ]