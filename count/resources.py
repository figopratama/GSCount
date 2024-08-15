from import_export import resources
from .models import UjiStasioner

class UjiStasionerResource(resources.ModelResource):
    class Meta:
        model = UjiStasioner