from django.contrib import admin
from .models import Size


class SizeAdmin(admin.ModelAdmin):
    list_display = ('category', 'friendly_name', 'name')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            # Only show categories that are assigned to at least one product
            kwargs["queryset"] = db_field.related_model.objects.filter(
                product__isnull=False
            ).distinct()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Size, SizeAdmin)
