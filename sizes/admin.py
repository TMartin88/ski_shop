from django.contrib import admin
from .models import Size, ProductSize


class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('product', 'size')
    list_filter = ('product', 'size')


admin.site.register(Size)
admin.site.register(ProductSize)
