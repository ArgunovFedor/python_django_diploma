from django.contrib.auth.views import LogoutView
from django.urls import path

from app_users.views import profile_view, account_view, register_view, CustomLoginView, profile_avatar_view, \
    restore_password

urlpatterns = [
    path('account/', account_view, name='account'),
    path('profile/', profile_view, name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profileAvatar/', profile_avatar_view, name='profile-avatar'),
    path('restore_password', restore_password, name='restore_password'),
]
