# Generated by Django 4.2.4 on 2023-09-05 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_postal_code_alter_order_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 5, 19, 51, 30, 767736)),
        ),
    ]
