from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
# from django.contrib.auth.decorators import login_required
=======
from django.contrib.auth.decorators import login_required
>>>>>>> origin/main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gscount.urls')),  # Assuming the home page is in gscount
<<<<<<< HEAD
    path('count/', include('count.urls')),
=======
    path('count/', include('crm.urls')),
    path('test/', include('test_technical_code.urls')),
>>>>>>> origin/main
]
