from django.contrib import admin
from .models import Size, ProductSize


class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('product', 'size', 'category')
    list_filter = ('category',)

    def category(self, obj):
        return obj.product.category


admin.site.register(Size)
admin.site.register(ProductSize, ProductSizeAdmin)
