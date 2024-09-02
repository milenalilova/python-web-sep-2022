from django.urls import path, include

from MyPlantApp.web.views import index, catalogue_page, profile_create, profile_details, profile_edit, profile_delete, \
    plant_create, plant_details, plant_edit, plant_delete

'''
http://localhost:8000/ - home page
http://localhost:8000/profile/create/ - profile create page
http://localhost:8000/catalogue/ - catalogue
http://localhost:8000/create/ - plant create page
http://localhost:8000/details/<plant_id>/ - plant details page
http://localhost:8000/edit/<plant_id>/ - plant edit page
http://localhost:8000/delete/<plant_id>/ - plant delete page
http://localhost:8000/profile/details/ - profile details page
http://localhost:8000/profile/edit/ - profile edit page
http://localhost:8000/profile/delete/ - profile delete page
'''

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue_page, name='catalogue'),
    path('profile/', include([
        path('create/', profile_create, name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),

    ])),

    path('details/<int:pk>/', plant_details, name='plant details'),
    path('create/', plant_create, name='plant create'),
    path('edit/<int:pk>/', plant_edit, name='plant edit'),
    path('delete/<int:pk>/', plant_delete, name='plant delete'),

)
