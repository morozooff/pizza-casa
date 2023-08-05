from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Profile {self.user.username}'