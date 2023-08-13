from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)