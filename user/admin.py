from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from rest_framework.authtoken.models import Token, TokenProxy

from user.models import Token, User , Notification

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    ordering = ["id"]
    list_display = ['id', "email", "first_name", "last_name", "phone_number", "user_type", "is_staff"]
    list_display_links = ['id', "email"]
    list_filter = ["user_type", 'is_staff', 'is_superuser', 'is_active', 'groups']
    search_fields = ["email", "first_name", "last_name", "user_type", "phone_number"]
    filter_horizontal= ['groups', 'friends']
    fieldsets = (
        (None, {
            "fields": ("email", "password"),
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_type'),
        }),
        ("Personal Information", {
            "fields": ("first_name", "middle_name", "last_name", "phone_number", "image", "friends"),
        }),
        ('Company Information', {
            'fields': (
                'company_name',
                'gst_number',
                'company_type',
                'company_address',
                'company_city',
                'company_state',
                'company_country',
                'company_pin_code',
            ),
        }),
        ('Package Information', {
            'fields': ('package_type','package_expiry'),
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined'),
        })
    )
    readonly_fields = ['date_joined', 'last_login']


admin.site.unregister(TokenProxy)
admin.site.register(Notification)
