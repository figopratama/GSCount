from django.contrib import admin
from django.urls import path, include
from . import views
from .views import style, team, partner

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('count.urls')),
    path('home/', views.home, name='home'),
    path('team/', views.team, name='team'),
    path('partner/', views.partner, name='partner'),
]
