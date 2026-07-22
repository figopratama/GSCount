from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from count.views import home, team, partner, style

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('home'), name='index'),
    path('', include('count.urls')),
    path('home/', home, name='home'),
    path('team/', team, name='team'),
    path('partner/', partner, name='partner'),
]
