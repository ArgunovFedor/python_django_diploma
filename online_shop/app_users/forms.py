from app_users.models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=False, label='Имя')
    last_name = forms.CharField(max_length=100, required=False, label='Фамилия')
    email = forms.EmailField(label='E-mail')
    date_of_birth = forms.DateTimeField(label='Дата рождения', widget=SelectDateWidget())
    city = forms.CharField(required=False, label='Город', max_length=36)
    patronymic = forms.CharField(max_length=100, required=False, label='Отчество')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'patronymic', 'email', 'password1', 'password2')


class RestorePasswordForm(forms.Form):
    email = forms.EmailField()


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', max_length=100, required=True)
    last_name = forms.CharField(label='Фамилия', max_length=100, required=True)
    email = forms.EmailField(label='E-mail', required=True)
    password = forms.CharField(label='Пароль', required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Тут можно изменить пароль'}), help_text='Оставьте пустым, если не хотите менять пароль')
    password_confirm = forms.CharField(label='Подтверждение пароля', required=False,
                                       widget=forms.TextInput(attrs={'placeholder': 'Введите пароль повторно'}))

    def __init__(self, *args, **kw):
        if 'instance' in kw.keys():
            self.base_fields['first_name'].initial = kw['instance'].user.first_name
            self.base_fields['last_name'].initial = kw['instance'].user.last_name
            self.base_fields['email'].initial = kw['instance'].user.email
        super(ProfileForm, self).__init__(*args, **kw)

    def save(self, *args, **kwargs):
        super(ProfileForm, self).save(*args, **kwargs)
        self.instance.user.first_name = self.cleaned_data.get('first_name')
        self.instance.user.last_name = self.cleaned_data.get('last_name')
        self.instance.user.email = self.cleaned_data.get('email')
        self.instance.patronymic = self.cleaned_data.get('patronymic')
        self.instance.avatar = self.cleaned_data.get('avatar')
        password = self.cleaned_data.get('password')
        if password is not '':
            self.instance.user.set_password(password)
        self.instance.save()

    class Meta:
        model = UserProfile
        fields = ['avatar', 'first_name', 'last_name', 'patronymic', 'phone_number', 'email', 'password',
                  'password_confirm']
