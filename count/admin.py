from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import UjiStasioner

# Register your models here.

@admin.register(UjiStasioner)
class HasilUjiAdmin(ImportExportModelAdmin):
    #list_display = ('ADF Statistics', 'P-Value', 'Critical Value')
    list_display = ('stat', 'value', 'crit')