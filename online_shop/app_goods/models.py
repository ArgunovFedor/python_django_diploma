from app_goods.forms import DELIVERY_METHODS, PAYMENT_METHODS
from app_users.models import User, UserProfile
from django.db import models
from django.urls import reverse


# Create your models here.
class Shop(models.Model):
    """
    Сущность для хранения данных о магазине
    """
    name = models.CharField(max_length=200, verbose_name='наименование')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Shop'


class Category(models.Model):
    """
    Категории товаров. Один товар может относиться к нескольким категориям
    """
    name = models.CharField(max_length=100, verbose_name='название')
    image = models.FileField(blank=True, verbose_name='иконки категорий', upload_to='images/icons')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Category'


class Good(models.Model):
    """
    Товар
    """
    name = models.CharField(max_length=200, verbose_name='наименование')
    description = models.CharField(max_length=400, verbose_name='описание')
    image = models.ImageField(verbose_name='изображение', upload_to='images/')
    # товар временно может быть без категории
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Good'


class Item(models.Model):
    """
    Товар конкретного магазина
    """
    # TODO: Дизайн сайта не предусматривает несколько поставщиков одного
    #  и того же товара по разным ценам. Поэтому стоит ли объединить сущность Item и Good в один Good
    code = models.CharField(max_length=100, verbose_name='артикул')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    count = models.IntegerField(verbose_name='количество')
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} {self.good.name}'

    class Meta:
        db_table = 'Item'

    def get_absolute_url(self):
        return reverse('product', args=[str(self.id)])


class Review(models.Model):
    """
    Отзывы
    """
    text = models.TextField(verbose_name='текст отзыва')
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str.join(str(self.good.id), self.good.name)

    class Meta:
        db_table = 'Review'


class ShoppingCart(models.Model):
    """
    Корзина
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(verbose_name='количество')

    class Meta:
        db_table = 'ShoppingCart'


class Order(models.Model):
    """
    История заказов
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=400, verbose_name='Описание')
    check_summ = models.DecimalField(max_digits=400, decimal_places=2, verbose_name='Сумма')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    city = models.CharField(verbose_name='Город', max_length=36)
    address = models.CharField(verbose_name='Адрес', max_length=150)
    delivery_method = models.CharField(max_length=2, choices=DELIVERY_METHODS, verbose_name='Тип доставки')
    payment_method = models.CharField(max_length=2, choices=PAYMENT_METHODS, verbose_name='Способ оплаты')
    account_number = models.IntegerField(null=True, verbose_name='номер счёта')
    is_success = models.BooleanField(default=True)

    class Meta:
        db_table = 'Order'

    def __str__(self):
        return ' '.join([str(self.id), self.user.username, self.created_at.strftime('%d/%m/%y')])

    def get_absolute_url(self):
        return reverse('one-order', args=[str(self.id)])

    def get_status_text(self):
        if self.is_success:
            return 'Оплачен'
        return 'Не оплачен'


class ShoppingCardItemLog(models.Model):
    """
    Журнал корзины. После операции оплаты сохраняется стоимость товара, так как оно может меняться со временем
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(verbose_name='количество')
    price = models.DecimalField(max_digits=400, decimal_places=2, verbose_name='сумма')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ShoppingCartLog'
