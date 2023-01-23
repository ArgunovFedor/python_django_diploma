from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Shop(models.Model):
    """
    Сущность для хранения данных о магазине
    """
    name = models.CharField(max_length=200, verbose_name='наименование')


class Good(models.Model):
    """
    Товар
    """
    name = models.CharField(max_length=200, verbose_name='наименование')
    description = models.CharField(max_length=400, verbose_name='описание')
    image = models.ImageField(verbose_name='изображение', upload_to='images/')


class Item(models.Model):
    """
    Товар конкретного магазина
    """
    code = models.CharField(max_length=100, verbose_name='артикул')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    count = models.IntegerField(verbose_name='количество')
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)


class ShoppingCart(models.Model):
    """
    Корзина
    """
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    count = models.IntegerField(verbose_name='количество')


class Order(models.Model):
    """
    История заказов
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    description = models.CharField(max_length=400, verbose_name='описание')
    check_summ = models.DecimalField(max_digits=400, decimal_places=2, verbose_name='сумма')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

