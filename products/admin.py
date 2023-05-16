from django.contrib import admin
from .models import Product, Category
from product_sizes.models import ProductSize


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1
    can_delete = True


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)
    inlines = [ProductSizeInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
