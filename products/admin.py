from django import forms
from django.contrib import admin
from .models import Product, Category
from sizes.models import Size
from product_sizes.models import ProductSize


class ProductSizeInlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        product = self.parent_object
        if product:
            # Get the category of the selected product
            category = product.category

            # Filter the sizes based on the selected product's category
            self.fields['size'].queryset = Size.objects.filter(category=category)

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
        'get_sizes',
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
