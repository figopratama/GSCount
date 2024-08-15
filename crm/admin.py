from django.contrib import admin
from . models import Date
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Date)
class DateAdmin(ImportExportModelAdmin):
    list_display = ('Clicks', 'Impressions', 'CTR', 'Ranking')
    
# admin.site.register(Date, ImportExportModelAdmin)

