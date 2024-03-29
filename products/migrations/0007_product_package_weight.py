# Generated by Django 3.2 on 2023-07-25 16:28

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20230614_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='package_weight',
            field=models.DecimalField(decimal_places=2, default=Decimal('5.00'), max_digits=6),
        ),
    ]
