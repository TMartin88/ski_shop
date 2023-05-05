# Generated by Django 3.2 on 2023-05-05 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
        ('checkout', '0004_order_weight_kg'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_method',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='shipping.shippingmethod'),
            preserve_default=False,
        ),
    ]
