from django.shortcuts import render


def account_view(request):
    return render(request, 'users/account.html')


def profile_view(request):
    return render(request, 'users/profile.html')


def login_view(request):
    return render(request, 'users/login.html')


def logout_view(request):
    return render(request, 'users/logout.html')


def profile_avatar_view(request):
    return render(request, 'users/profileavatar.html')
