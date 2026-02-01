from django.contrib import admin
from .models import SnackCompra
# Register your models here.

@admin.register(SnackCompra)
class SnackcompraAdmin(admin.ModelAdmin):
    pass