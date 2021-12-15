from django.contrib import admin
from paranoid_model.admin import ParanoidAdmin

from payment.models import Payment

@admin.register(Payment)
class PaymentAdmin(ParanoidAdmin):
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
                "fields": ["created_at", "updated_at", "deleted_at"]
            },
        ),
    )
    readonly_fields = ("created_at", "updated_at", "deleted_at")
    