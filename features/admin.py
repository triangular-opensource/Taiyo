from django.contrib import admin
from .models import Category,  Product, CategoryFields

admin.site.register(CategoryFields)
admin.site.register(Product)
admin.site.register(Category)
