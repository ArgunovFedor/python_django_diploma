from app_goods.models import Item
from django.shortcuts import render


def index_view(request):
    # TODO: Доделать выборку
    context = {
        'popular_product': Item.objects.order_by('-updated_at')[:10],
        'limited_edition': Item.objects.all()[:10],
        'discounted_products': Item.objects.all()[:3],
    }
    return render(request, 'index.html', context=context)


def about_view(request):
    return render(request, 'about.html')


def error_view(request, error_code):
    """
    Страница вывода теста ошибки
    :param request:
    :param error_code:
    :return:
    """
    from django.conf import settings
    if error_code in settings.ERROR_DICT:
        error_message = settings.ERROR_DICT[error_code]
    else:
        error_message = 'Что-то произошло не так'
    return render(request, 'error.html', context={
        'error_message': error_message
    })
