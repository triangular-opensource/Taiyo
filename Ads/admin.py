from django.contrib import admin

from Ads.models import Advertisement, Bid

class AdAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'product', 'category', 'timestamp']
    list_display_links = ["__str__", "product", "category"]
    readonly_fields = [
        'category',
        'image_1_display',
        'image_2_display',
        'image_3_display',
        'image_4_display',
        "bidding_close_date",
    ]
    fieldsets = (
        (None, {
            "fields": (
                "buy_or_sell",
                'product',
                'category',
                "product_description",
                "basic_price",
                "user"
            ),
        }),
        ("Product Specification", {
            "fields": (
                "quality",
                "dimentions",
                "grade",
                "temper",
                "specification_number",
                "quantity",
                "coating_in_gsm",
                "color"
            )
        }),
        ("Bidding Data", {
            "fields": (
                "bidding",
                "bidding_close_date",
                "selected_bid"
            )
        }),
        ("Files", {
            "fields": (
                "image_1",
                "image_1_link",
                "image_1_display",
                "image_2",
                "image_2_link",
                "image_2_display",
                "image_3",
                "image_3_link",
                "image_3_display",
                "image_4",
                "image_4_link",
                "image_4_display",
                "excel_file",
                "excel_file_link",
                "pdf_file",
                "pdf_file_link",
            ),
        }),
        ("Author Details", {
            "fields": (
                "name",
                "mobile_number",
                "business_address",
                "location"
            )
        })
    )


class BidAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'user', 'advertisement', 'selected']
    list_display_links = ['id', 'amount']
    list_filter = ['advertisement', 'selected']

admin.site.register(Advertisement, AdAdmin)
admin.site.register(Bid, BidAdmin)