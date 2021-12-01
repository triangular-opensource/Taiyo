from django.contrib import admin

from .models import GeneralInfo, Addres, Policy, NewsLetter

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact']
    list_display_links = ['name']
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'contact', 'copyright',)
        }),
        ('Images', {
            'fields': ('icon', 'cover_image',)
        }),
        ('About', {
            'fields': (
                'intro', 'about',)
        }),
        ('Links', {
            'fields': (
                'twitter', 'linked_in', 'facebook',)
        }),
        ('Mobile App Links', {
            'fields': (
                'android_store', 'apple_store',)
        }),
    )

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)
 
@admin.register(Addres)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['address', 'city', 'state', 'country', 'pincode']
    list_display_links = ['address']


    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ['terms_and_condition', 'privacy_policies']
    list_display_links = ['terms_and_condition', 'privacy_policies']

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)

@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'generation_time']
    list_display_links = ['id', 'email']
