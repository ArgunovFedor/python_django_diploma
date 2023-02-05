from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=100, required=False, help_text='Фамилия')
    email = forms.EmailField()
    date_of_birth = forms.DateTimeField(widget=SelectDateWidget())
    city = forms.CharField(required=False, help_text='Город', max_length=36)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class RestorePasswordForm(forms.Form):
    email = forms.EmailField()

