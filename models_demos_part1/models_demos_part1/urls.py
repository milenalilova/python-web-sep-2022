from django.contrib import admin
from django.urls import path, include

import models_demos_part1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('models_demos_part1.web.urls'))
]
