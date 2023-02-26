from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    date_of_birth = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=36, blank=True)
    balance = models.IntegerField(default=0, verbose_name='Balance')
    avatar = models.ImageField(blank=True, verbose_name='аватарка профиля', upload_to='images/avatars')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество')
    phone_number = PhoneNumberField(null=True, blank=True, unique=True, verbose_name='Номер телефона')

    class Meta:
        db_table = 'UserProfile'
