from django.db import models
from products.models import Product, Category
from sizes.models import Size


class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_sizes')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} - {self.size}"
