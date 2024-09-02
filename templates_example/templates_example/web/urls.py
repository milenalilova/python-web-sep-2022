from django.urls import path

from templates_example.web.views import index, redirect_to_home

urlpatterns = (
    path('', index, name='index'),
    path('go-to-home/', redirect_to_home, name='redirect to home'),
)
