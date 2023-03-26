import json

from app_goods.forms import OrderForm
from app_goods.models import (Good, Item, Order, Review, ShoppingCardItemLog,
                              ShoppingCart)
from app_goods.utils import try_parse_int
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from rolepermissions.decorators import has_role_decorator


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


def payment_view(request, id):
    return render(request, 'goods/payment.html', {"order_id": id})


def payment_someone_view(request, id):
    return render(request, 'goods/paymentsomeone.html', {"order_id": id})


class ProductDetailView(DetailView):
    model = Good
    template_name = 'goods/product.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        # у одного товара может быть несколько артиклов и разная цена, но ради упращения
        # будем брать первый попавшийся
        context['item'] = Item.objects.filter(good=context['good']).first()
        context['reviews'] = Review.objects.filter(good=context['good']).select_related('author').select_related(
            'author__userprofile').all()
        return context


def progress_payment_view(request):
    if request.method == 'POST':
        id = request.POST['order_id']
        account_number = request.POST['numero1']
        order_item = Order.objects.filter(id=id).first()
        order_item.account_number = int(account_number.replace(' ', ''))
        order_item.is_success = True
        order_item.save()
        # очистить корзину
        ShoppingCart.objects.filter(user_id=request.user.id).delete()
    return render(request, 'goods/progressPayment.html')


def sale_view(request):
    return render(request, 'goods/sale.html')


@has_role_decorator('client')
def history_order_view(request):
    items = Order.objects.filter(user_id=request.user.id).all()
    return render(request, 'order/historyorder.html', context={
        'items': items
    })


@has_role_decorator('client')
def one_order_view(request, id):
    """
    История заказов. Подробная история
    :param request:
    :param id:
    :return:
    """
    # защита от перебора
    if Order.objects.filter(id=id, user=request.user).exists():
        order_item = Order.objects.filter(id=id).first()
        shopping_card_item_logs = ShoppingCardItemLog.objects.filter(order_id=id).all()
        return render(request, 'order/oneorder.html', context={
            'order_item': order_item,
            'shopping_card_items': shopping_card_item_logs
        })
    return redirect('error', 'ORDER_01')


@has_role_decorator('client')
def order_view(request, *args, **kwargs):
    items = ShoppingCart.objects.filter(user_id=request.user.id).select_related('item').all()
    all_sum = sum([cart.item.price * cart.count for cart in items])
    if items.count() == 0:
        return redirect('error', 'ORDER_02')
    # берет текущий шаг из uri
    if 'pk' in kwargs:
        step_id = kwargs['pk']
    else:
        step_id = 1
    if request.method == 'POST':
        form = OrderForm(post=request.POST, userprofile=request.user.userprofile)
        if request.POST.get('is_final_click'):
            # Берем нужные поля с формы
            city = form.base_fields['city'].initial
            address = form.base_fields['address'].initial
            delivery_method = form.base_fields['delivery_method'].initial
            payment_method = form.base_fields['payment_method'].initial
            # Сохраняем в истории заказов
            order_item = Order.objects.create(user_id=request.user.id, description='', check_summ=all_sum,
                                              city=city, address=address,
                                              delivery_method=delivery_method[1],
                                              payment_method=payment_method[1], is_success=False)
            item_logs = [ShoppingCardItemLog(item=item.item, count=item.count, price=item.item.price, order=order_item)
                         for item in items]
            ShoppingCardItemLog.objects.bulk_create(item_logs)

            if payment_method[0] is '1':
                # онлайн картой
                return redirect('payment', order_item.id)
            elif payment_method[0] is '2':
                # онлайн со случайного счёта
                return redirect('payment-someone', order_item.id)
    else:
        form = OrderForm(userprofile=request.user.userprofile)
    if request.POST.get('next_step') and form.is_valid() is not None:
        # берем параметр следующего шага из кнопки
        step_id = int(request.POST.get('next_step'))

    return render(request, 'order/order.html', {
        'form': form,
        "items": items,
        "all_sum": all_sum,
        'step_id': step_id
    })


@has_role_decorator('client')
def add_cart_item_view(request, *args, **kwargs):
    """
    Добавляет товар в корзину
    :param product_id: Идентификатор продукта
    :param request:
    :return:
    """
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


def add_review(request, id):
    if request.method == 'POST':
        text = request.POST['review']
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        Review.objects.create(text=text, author=user, good_id=id)
    return redirect('product', id)
