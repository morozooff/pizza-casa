from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Profile
# Register your models here.


@register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'points',]
