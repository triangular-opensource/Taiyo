from django.contrib import admin

# Register your models here.
from .models import GenralInfo, Addres, Policy, NewsLetter

admin.site.register(GenralInfo)
admin.site.register(Addres)
admin.site.register(Policy)
admin.site.register(NewsLetter)
