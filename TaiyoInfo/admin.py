from django.contrib import admin

from .models import GenralInfo, Addres, Policy, NewsLetter

@admin.register(GenralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact']
    list_display_links = ['name']
 



admin.site.register(Addres)
admin.site.register(Policy)
admin.site.register(NewsLetter)
