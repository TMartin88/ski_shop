# Generated by Django 3.2 on 2023-07-26 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_order_flat_fee_applied'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_method',
            field=models.CharField(default='Standard Shipping', max_length=255),
        ),
    ]