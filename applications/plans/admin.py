from django.contrib import admin
from django.utils import timezone
from .models import *
# Register your models here.

# admin.site.register(Prueba)

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ("name", "description", "instrument", "price"),
        }),
    )