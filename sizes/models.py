from django.db import models
from products.models import Product


class Size(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category} - {self.name}"

    def get_friendly_name(self):
        return self.friendly_name


class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_sizes')
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} - {self.size}"
