"""
URL configuration for gscount project.

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
=======
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
>>>>>>> origin/main
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import style, team, partner

<<<<<<< HEAD
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('count.urls')),

    path('home/', views.home, name='home'),
    path('team/', views.team, name='team'),
    path('partner/', views.partner, name='partner'),
    path('', views.home, name='home'),
]
=======


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
    
    path('team/', views.team, name='team'),
    path('partner/', views.partner, name='partner'),
    path('home/', views.home, name='home'),
    path('test/', views.index, name='index'),
    path('', views.home, name='home'),
    


    
    # path('upload/', views.upload, name='upload'),
    # path('register/', views.register, name='register'),
    # path('logout/', views.logout, name='logout'),
    # path('', include('gscount.urls')),
    # path('run_adfuller/', views.run_adfuller, name='run_adfuller'),
]

>>>>>>> origin/main
