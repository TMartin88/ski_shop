# Generated by Django 3.2 on 2023-06-09 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20230516_1141'),
        ('product_sizes', '0004_alter_productsize_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsize',
            name='category',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
    ]
