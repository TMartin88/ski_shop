from django.db import models
from django_countries.fields import CountryField


class ShippingCost(models.Model):
    country = CountryField()
    weight_from = models.DecimalField(max_digits=6, decimal_places=2)
    weight_to = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return (
                f"{self.country} ({self.weight_from}kg - {self.weight_to}kg): "
                f"${self.cost}"
        )
