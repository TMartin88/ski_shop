from django.contrib import admin
from .models import Product, Category
from product_sizes.models import ProductSize
from sizes.models import Size
from django.forms import BaseInlineFormSet


class ProductSizeFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter sizes based on the selected product's category
        self.queryset = Size.objects.filter(category=self.instance.category)


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1
    formset = ProductSizeFormSet


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
