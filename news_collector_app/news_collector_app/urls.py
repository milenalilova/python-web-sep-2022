from django.contrib import admin
from django.urls import path, include

import news_collector_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news_collector_app.web.urls')),
]
