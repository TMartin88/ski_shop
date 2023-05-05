from django.contrib import admin
from .models import ShippingMethod, ShippingCost


@admin.register(ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'active']
    list_filter = ['active']


@admin.register(ShippingCost)
class ShippingCostAdmin(admin.ModelAdmin):
    list_display = ['country', 'weight_from', 'weight_to', 'cost', 'method']
    list_filter = ['country', 'method']
