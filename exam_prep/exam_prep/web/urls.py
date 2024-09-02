from django.urls import path, include

from exam_prep.web.views import index, add_album, delete_album, edit_album, details_album, details_profile, \
    delete_profile, add_profile

urlpatterns = (
    path('', index, name='index'),
    path('album/', include([
        path('add/', add_album, name='add album'),
        path('details/<int:pk>/', details_album, name='details album'),
        path('delete/<int:pk>/', delete_album, name='delete album'),
        path('edit/<int:pk>/', edit_album, name='edit album'),
    ])),
    path('profile/', include([
        path('add/', add_profile, name='add profile'),
        path('details/', details_profile, name='details profile'),
        path('delete/', delete_profile, name='delete profile')
    ])),

)
