from django.urls import path
from . import views



urlpatterns = [
    path('count/', views.upload_and_count, name='upload_and_count'),
    path('delete_data/', views.delete_data, name='delete_data'),

]