from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Product, Category


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['title', ]


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'base_cost', 'description', 'avatar', 'category', 'ingredients', ]
