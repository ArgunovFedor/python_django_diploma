import json

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from rolepermissions.decorators import has_role_decorator

from app_goods.models import Item, ShoppingCart, Good, Review
from app_goods.utils import try_parse_int


# Create your views here.

def cart_view(request):
    """
    Для отображения корзины
    :param request:
    :return:
    """
    items = ShoppingCart.objects.filter(user_id=request.user.id).select_related('item').all()
    all_sum = sum([cart.item.price * cart.count for cart in items])
    context = {
        "items": items,
        "all_sum": all_sum
    }
    return render(request, 'goods/cart.html', context)


class CatalogListView(ListView):
    """
    Для отображения каталога товаров
    :param ListView:
    :return:
    """
    # в шаблоне пагинация в среднем по 8 товаров
    # Есть сортировка по популярности, новизне, отзывам,
    # а также по ценовому диапазону и тэгам
    # думаю, что правильнее реализовать через метод GET и входным параметрам кроме кнопки FILTER
    model = Item
    paginate_by = 10
    template_name = 'goods/catalog.html'

    def get_context_data(self, **kwargs):
        context = super(CatalogListView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', 'give-default-value')
        context['orderby'] = self.request.GET.get('orderby', 'give-default-value')
        return context

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', None)
        order = self.request.GET.get('orderby', 'price')
        if filter_val is not None:
            new_context = Item.objects.filter(
                good__category__name=filter_val,
            ).order_by(order)
        else:
            new_context = Item.objects.order_by(order)
        return new_context


def payment_view(request):
    return render(request, 'goods/payment.html')


def payment_someone_view(request):
    return render(request, 'goods/paymentsomeone.html')


class ProductDetailView(DetailView):
    model = Good
    template_name = 'goods/product.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        # у одного товара может быть несколько артиклов и разная цена, но ради упращения
        # будем брать первый попавшийся
        context['item'] = Item.objects.filter(good=context['good']).first()
        context['reviews'] = Review.objects.filter(good=context['good']).select_related('author').select_related('author__userprofile').all()
        return context

def progress_payment_view(request):
    return render(request, 'goods/progressPayment.html')


def sale_view(request):
    return render(request, 'goods/sale.html')


def history_order_view(request):
    return render(request, 'order/historyorder.html')


def one_order_view(request):
    return render(request, 'goods/oneorder.html')


def order_view(request):
    return render(request, 'order/order.html')


@has_role_decorator('client')
def add_cart_item_view(request, *args, **kwargs):
    """
    Добавляет товар в корзину
    :param product_id: Идентификатор продукта
    :param request:
    :return:
    """
    print(request.user.user_permissions.all())
    if request.method == 'GET':
        item_id = request.GET['product_id']
        count_from_get = request.GET.get('count')
        if count_from_get is not None:
            count = try_parse_int(request.GET['count'])
        else:
            count = 1
        item = ShoppingCart.objects.filter(user_id=request.user.id, item_id=item_id).first()
        if item is None:
            ShoppingCart.objects.create(user_id=request.user.id, item_id=item_id, count=count)
            return redirect('cart')
        item.count += count
        item.save(update_fields=['count'])
    # Обновляем страницу из которой клиент передал запрос, чтобы иконка корзины обновилась
    if 'filters' not in request.GET:
        return redirect('cart')
    filters = request.GET['filters']
    json_acceptable_string = filters.replace("'", "\"")
    filters = json.loads(json_acceptable_string)
    return HttpResponseRedirect(reverse('catalog') + '?' + urlencode(filters))


@has_role_decorator('client')
def delete_cart_item_view(request, *args, **kwargs):
    """
    Метод удаляет из корзины элемент
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    item_id = kwargs['product_id']
    if request.method == 'GET':
        ShoppingCart.objects.filter(user_id=request.user.id, id=item_id).delete()
    return redirect('cart')
