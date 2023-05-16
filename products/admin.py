from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from .models import Product, Category
from product_sizes.models import ProductSize
from sizes.models import Size


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "size":
            # Check if the product being edited already has ProductSize entries
            if request.resolver_match.view_name == 'admin:products_product_change':
                product_id = request.resolver_match.kwargs.get('object_id')
                try:
                    product = Product.objects.get(pk=product_id)
                    kwargs["queryset"] = Size.objects.filter(category=product.category)
                except Product.DoesNotExist:
                    pass
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def delete_queryset(self, request, queryset):
        # Override delete_queryset to delete entries from the ProductSize model
        for obj in queryset:
            try:
                obj.delete()
            except ObjectDoesNotExist:
                pass


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
