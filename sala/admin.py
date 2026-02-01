from django.contrib import admin
from .models import Sala
# Register your models here.

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    pass
