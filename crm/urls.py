from django.urls import path
from . import views
from . import example



urlpatterns = [
    path('count/', views.upload_and_count, name='upload_and_count'),
    path('delete_data/', views.delete_data, name='delete_data'),
    

    
    # path('count/', views.upload, name='upload'),
    # path('count/', views.count, name='count'),
    # path('alldata/', views.alldata, name='alldata'),
    # path('adfuller/', example.adfuller, name='adfuller'),

]