from django.db import models
from PIL import Image as Im
#
# class Modification(models.Model):
#     title = models.CharField(max_length=100, primary_key=True)
#     cost = models.PositiveIntegerField()

class Category(models.Model):
    title = models.CharField(max_length=100, primary_key=True)


class Product(models.Model):
    title = models.CharField(max_length=255)
    base_cost = models.PositiveIntegerField()
    description = models.TextField()
    avatar = models.ImageField(upload_to = 'images/')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def save(self):
        super().save()
        image = Im.open(self.avatar.path)
        if image.height > 300 or image.width > 300:
            correct_params = (300, 300)
            image.thumbnail(correct_params)
            image.save(self.avatar.path)

