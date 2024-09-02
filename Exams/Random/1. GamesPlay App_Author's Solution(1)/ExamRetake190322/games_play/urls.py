from django.urls import path, include

from games_play import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('dashboard/', views.dashboard_page, name='dashboard-page'),
    path('profile/', include([
        path('create/', views.create_profile_page, name='create-profile-page'),
        path('details/', views.profile_details_page, name='profile-details-page'),
        path('edit/', views.edit_profile_page, name='edit-profile-page'),
        path('delete/', views.delete_profile_page, name='delete-profile-page'),
    ])),
    path('game/', include([
        path('create/', views.create_game_page, name='create-game-page'),
        path('details/<int:game_id>', views.game_details_page, name='game-details-page'),
        path('edit/<int:game_id>', views.edit_game_page, name='edit-game-page'),
        path('delete/<int:game_id>', views.delete_game_page, name='delete-game-page'),
    ])),
]
