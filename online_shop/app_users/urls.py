from app_users.views import (CustomLoginView, account_view,
                             profile_avatar_view, profile_view, register_view,
                             restore_password)
from django.contrib.auth.views import LogoutView
from django.urls import path

urlpatterns = [
    path('account/', account_view, name='account'),
    path('profile/', profile_view, name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profileAvatar/', profile_avatar_view, name='profile-avatar'),
    path('restore_password', restore_password, name='restore_password')
]
