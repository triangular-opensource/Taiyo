from django.contrib import admin
from django.http import HttpResponse, HttpResponseForbidden

from .models import GeneralInfo, Addres, Policy, NewsLetter , Category , Product , Subscription , Contact
import csv



@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'phone_number']
    list_display_links = ['name']
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone_number', 'copyright',)
        }),
        ('Images', {
            'fields': ('icon','icon_link', 'icon_tag', 'cover_image','cover_image_link','cover_tag')
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
    readonly_fields = ['icon_tag', 'cover_tag']
    actions = ['download_csv']

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


admin.site.register(Category)
admin.site.register(Product)



@admin.register(Contact)
class Constactdmin(admin.ModelAdmin):
    list_display = ['id', 'name','email' , 'subject']
    list_display_links = ['id', 'name' , 'email' , 'subject']



@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['name','amount','days']
    list_display_links = ['name','amount','days']

















