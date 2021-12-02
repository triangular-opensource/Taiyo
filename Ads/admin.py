from django.contrib import admin

from Ads.models import Advertisement, Category, Product

# Register your models here.
class AdAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'category']
    readonly_fields = ['category']
    fieldsets = (
        (None, {
            "fields": (
                'product', 'category'
            ),
        }),
    )
    
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Advertisement, AdAdmin)