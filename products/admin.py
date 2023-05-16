from django import forms
from django.contrib import admin
from .models import Product, Category
from product_sizes.models import ProductSize


class ProductSizeInlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        product = self.instance.product if self.instance else None
        if product:
            # Filter the sizes based on the selected product's category
            category = product.category
            self.fields['size'].queryset = self.fields['size'].queryset.filter(category=category)

    class Meta:
        model = ProductSize
        fields = '__all__'


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    form = ProductSizeInlineForm


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSizeInline]


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


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
