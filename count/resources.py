from import_export import resources
from .models import Date

class DateResource(resources.ModelResource):
    class Meta:
        model = Date
        # db_table = "date_model"