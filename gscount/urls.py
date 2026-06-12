from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from . import views
from .views import style, team, partner

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('home'), name='index'),
    path('', include('count.urls')),
    path('home/', views.home, name='home'),
    path('team/', views.team, name='team'),
    path('partner/', views.partner, name='partner'),
]
