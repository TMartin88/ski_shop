# Generated by Django 3.2 on 2023-05-04 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_has_colors'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Weight of the product in kilograms.', max_digits=6),
        ),
    ]
