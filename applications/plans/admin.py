from django.contrib import admin
from django.utils import timezone
from .models import *
# Register your models here.

# admin.site.register(Prueba)
admin.site.register(Plan)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass