from django.urls import path
from app_users.views import profile_view, account_view, login_view, logout_view, profile_avatar_view

urlpatterns = [
    path('account/', account_view, name='account'),
    path('profile/', profile_view, name='profile'),
    #path('login/', login_view, name='login'),
    #path('logout/', logout_view, name='logout'),
    path('profileAvatar/', profile_avatar_view, name='profile-avatar'),
]