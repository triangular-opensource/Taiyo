import csv

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.http import HttpResponse, HttpResponseForbidden
from rest_framework.authtoken.models import TokenProxy

from user.models import Token, User , Notification

@admin.register(User)
class UserAdmin(BaseUserAdmin):

    @admin.action(description="download csv")
    def download_csv(modeladmin, request, queryset):
        try:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="user.csv"'

            writer = csv.writer(response)
            writer.writerow([])
            writer.writerow([
                "id",
                "first_name",
                "middle_name",
                "last_name",
                "email",
                "image",
                "gst_number",
                "phone_number",
                "user_type",
                "package_type",
                "package_expiry",
                "company_name",
                "company_type",
                "company_address",
                "company_city",
                "company_state",
                "company_country",
                "company_pin_code",
                "last_login",
                "date_joined"
            ])
            for s in queryset:
                writer.writerow([
                    s.id,
                    s.first_name,
                    s.middle_name,
                    s.last_name,
                    s.email,
                    s.image,
                    s.gst_number,
                    s.phone_number,
                    s.user_type,
                    s.package_type,
                    s.package_expiry,
                    s.company_name,
                    s.company_type,
                    s.company_address,
                    s.company_city,
                    s.company_state,
                    s.company_country,
                    s.company_pin_code,
                    s.last_login,
                    s.date_joined
                ])
            return response
        except Exception as err:
            return HttpResponseForbidden("<h1>403 Not Authorized</h1>")

    actions = [download_csv]
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
