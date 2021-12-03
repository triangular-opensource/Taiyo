from django.contrib import admin

from Ads.models import Advertisement , Bid , AdImages

# class AdAdmin(admin.ModelAdmin):
#     list_display = ['id', 'product', 'category']
#     readonly_fields = ['category']
#     fieldsets = (
#         (None, {
#             "fields": (
#                 'product', 'category'
#             ),
#         }),
#     )

admin.site.register(Advertisement)
admin.site.register(Bid)
admin.site.register(AdImages)