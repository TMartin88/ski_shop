from django.contrib import admin
from .models import ProductSize


class ProductSizeAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductSize, ProductSizeAdmin)
