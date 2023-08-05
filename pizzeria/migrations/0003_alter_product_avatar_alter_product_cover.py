# Generated by Django 4.2.4 on 2023-08-05 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0002_product_cover_product_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='avatar',
            field=models.ImageField(default='default-product-image.png', upload_to='images/avatars/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cover',
            field=models.ImageField(default='default-product-image.png', upload_to='images/covers/'),
        ),
    ]