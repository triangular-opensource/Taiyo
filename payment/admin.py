import csv

from django.contrib import admin
from django.http import HttpResponse, HttpResponseForbidden

from payment.models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'package', 'paid']
    list_display_links = ['id', 'user']
    search_fields = list_display
    list_filter = ['paid']
    fieldsets = (
        (
            None,
            {
                "fields": ["user", "amount", "package", "paid"],
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

    @admin.action(description="download csv")
    def download_csv(modeladmin, request, queryset):
        try:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="user.csv"'

            writer = csv.writer(response)
            writer.writerow([])
            writer.writerow(['id', 'user', 'amount', 'order_id', 'payment_id', 'package', 'paid', 'timestamp'])
            for s in queryset:
                writer.writerow([s.id, s.user, s.amount, s.order_id, s.payment_id, s.package, s.paid,s.timestamp])
            return response
        except Exception as err:
            return HttpResponseForbidden("<h1>403 Not Authorized</h1>")

    actions = [download_csv]
    