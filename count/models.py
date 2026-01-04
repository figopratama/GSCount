from django.db import models

# Create your models here.
class Date(models.Model):

    Date = models.CharField(max_length=150)
    Clicks = models.CharField(max_length=100)
    Impressions = models.CharField(max_length=100)
    Ranking = models.CharField(max_length=100)
    CTR = models.CharField(max_length=100)
    Release_Date = models.DateField(null=True)

    def __str__(self):
        return self.Date
    
    class Meta:
        db_table = "date_model"

class ADFResult(models.Model):
    variable_name = models.CharField(max_length=100)
    adf_statistic = models.FloatField()
    p_value = models.FloatField()
    # stationery_test = models.CharField(max_length=100)
    critical_value_1 = models.FloatField()
    critical_value_5 = models.FloatField()
    critical_value_10 = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.variable_name