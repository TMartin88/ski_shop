from django import forms
from django.contrib import admin
from .models import Product, Category
from sizes.models import Size
from product_sizes.models import ProductSize


class ProductSizeInlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # If the product is not selected yet
        if not self.instance.product_id:
            # Set the queryset of the size field to an empty list
            self.fields['size'].queryset = Size.objects.none()

    class Meta:
        model = ProductSize
        fields = '__all__'


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    form = ProductSizeInlineForm
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSizeInline]

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
