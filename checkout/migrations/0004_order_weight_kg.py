# Generated by Django 3.2 on 2023-05-05 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20230426_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='weight_kg',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
