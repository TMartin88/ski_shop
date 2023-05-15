from django.contrib import admin
from .models import Size, ProductSize


class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('product', 'size')
    list_filter = ('product__category', 'size__category')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "size":
            # Only show sizes that are assigned to the same category
            #  as the product
            product_id = request.GET.get('product')
            if product_id:
                product = Product.objects.get(id=product_id)
                kwargs["queryset"] = db_field.related_model.objects.filter(
                    category=product.category
                )
            else:
                kwargs["queryset"] = db_field.related_model.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(ProductSize, ProductSizeAdmin)
