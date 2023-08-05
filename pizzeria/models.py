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
    avatar = models.ImageField(upload_to = 'images/avatars/', default='default-product-image.png')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    ingredients = models.TextField(blank=True, null = True)

    # def save(self, *args, **kwargs):
    #
    #     super(Product, self).save(*args, **kwargs)
    #
    #     cover_path = self.cover.path
    #     cover_image = Im.open(cover_path)
    #     if cover_image.height > 300 or cover_image.width > 300:
    #         correct_params = (300, 300)
    #         cover_image.thumbnail(correct_params)
    #         cover_image.save(cover_path)
    #
    #     avatar_path = self.avatar.path
    #     avatar_image = Im.open(avatar_path)
    #     if avatar_image.height > 500 or avatar_image.width > 340:
    #         correct_avatar_params = (500, 340)
    #         avatar_image.thumbnail(correct_avatar_params)
    #         avatar_image.save(avatar_path)




