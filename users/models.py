from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name='profile')
    points = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=40, default="Moscow, Pizzeria Pizza-Casa")

    def __str__(self):
        return f'Profile {self.user.username}'