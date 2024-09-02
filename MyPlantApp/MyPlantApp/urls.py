from django.contrib import admin
from django.urls import path, include

import MyPlantApp

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('MyPlantApp.web.urls')),
]
