from django.db import models
from django_countries.fields import CountryField


class ShippingMethod(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ShippingCost(models.Model):
    country = CountryField()
    weight_from = models.DecimalField(max_digits=6, decimal_places=2)
    weight_to = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    method = models.ForeignKey(
        'shipping.ShippingMethod',
        on_delete=models.CASCADE
        )

    def __str__(self):
        return (
                f"{self.country} ({self.weight_from}kg - {self.weight_to}kg): "
                f"${self.cost} - {self.method}"
        )

    def get_cost(self):
        return self.cost
