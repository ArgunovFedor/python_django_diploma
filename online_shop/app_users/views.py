from app_goods.models import Order
from app_users.forms import ProfileForm, RegisterForm, RestorePasswordForm
from app_users.models import UserProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from rolepermissions.decorators import has_role_decorator
from rolepermissions.roles import assign_role


@has_role_decorator('client')
def account_view(request):
    item = Order.objects.filter(user_id=request.user.id).order_by('created_at').last()
    return render(request, 'users/account.html', context={
        'item': item
    })

@has_role_decorator('client')
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            password_confirm = form.cleaned_data.get('password_confirm')
            if password != password_confirm:
                form.add_error('password', 'Пароль и пароль подтверждения должны быть одинаковыми')
                form.add_error('password_confirm', 'Пароль и пароль подтверждения должны быть одинаковыми')
                return render(request, 'users/profile.html', {'form': form})
            form.save()
            return render(request, 'users/profile.html', {'form': form})
    else:
        form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'users/profile.html', {'form': form})


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('index')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        """
        Ограничиваем доступ к сайту суперпользователей
        :param form:
        :return:
        """
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active and not user.is_superuser:
                login(self.request, user)
                return HttpResponseRedirect(redirect_to='/')
            else:
                form.add_error('__all__', 'Ошибка. Учетная запись пользователя не активна')
        else:
            form.add_error('__all__', 'Ошибка! проверьте написания логина и пароля')
        return self.render_to_response(self.get_context_data(form=form))


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            row_password = form.cleaned_data.get('password1')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            patronymic = form.cleaned_data.get('patronymic')
            user = authenticate(username=username, password=row_password, date_of_birth=date_of_birth, city=city)
            UserProfile.objects.create(user=user, date_of_birth=date_of_birth, city=city, balance=0,
                                       patronymic=patronymic,
                                       avatar='images/avatars/default.png')
            assign_role(user, 'client')
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def profile_avatar_view(request):
    return render(request, 'users/profileavatar.html')


def restore_password(request):
    if request.method == 'POST':
        form = RestorePasswordForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            new_password = User.objects.make_random_password()
            current_user = User.objects.filter(email=user_email).first()
            if current_user:
                current_user.set_password(new_password)
                current_user.save()
            send_mail(
                subject='Восстановление пароля',
                message=f'Ваш новый пароль: {new_password}',
                from_email='fargunov@internet.ru',
                recipient_list=[form.cleaned_data['email']]
            )
            return render(request, 'helpers/page_with_some_text.html', context={
                'title': 'Успех',
                'some_text': 'Письмо с первым паролем было успешно отправлено'
            })
    restore_password_form = RestorePasswordForm()
    context = {
        'form': restore_password_form
    }
    return render(request, 'users/restore_password.html', context=context)
