# Generated by Django 4.2.4 on 2023-09-05 18:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='place_of_issue',
            field=models.CharField(choices=[('IP', 'In Pizzeria'), ('DYA', 'Delivery on Your Own Address')], default='IP', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 5, 18, 56, 47, 192798)),
        ),
    ]
