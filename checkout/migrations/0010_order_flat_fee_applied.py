# Generated by Django 3.2 on 2023-07-26 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_alter_orderlineitem_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='flat_fee_applied',
            field=models.BooleanField(default=False),
        ),
    ]
