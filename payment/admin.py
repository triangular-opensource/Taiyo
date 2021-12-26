import csv

from django.contrib import admin
from django.http import HttpResponse, HttpResponseForbidden

from payment.models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    @admin.action(description="download csv")
    def download_csv(modeladmin, request, queryset):
        try:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="payment.csv"'

            writer = csv.writer(response)
            writer.writerow([])
            writer.writerow([
            'user' 
            'amount',
            'order_id',
            'payment_id',
            'payment_signature',
            'timestamp',
            'paid'
            ])
            for s in queryset:
                writer.writerow([s.name, s.email, s.phone_number])
            return response
        except Exception as err:
            return HttpResponseForbidden("<h1>403 Not Authorized</h1>")







    list_display = ['id', 'user', 'amount', 'paid']
    list_display_links = ['id', 'user']
    search_fields = list_display
    list_filter = ['paid']
    fieldsets = (
        (
            None,
            {
                "fields": ["user", "amount", "paid"],
            }
        ),
        (
            "Payment Details",
            {
                "fields": ["order_id", "payment_id", "payment_signature"]
            }
        ),
        (
            "Important Dates",
            {
                "fields": ["timestamp",]
            },
        ),
    )
    readonly_fields = ("timestamp",)
