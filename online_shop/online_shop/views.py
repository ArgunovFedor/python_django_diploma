from app_goods.models import Item
from django.shortcuts import render


def index_view(request):
    # TODO: Доделать выборку
    context = {
        'popular_product': Item.objects.order_by('-updated_at')[:10],
        'limited_edition':  Item.objects.all()[:10],
        'discounted_products': Item.objects.all()[:3],
    }
    return render(request, 'index.html', context=context)

def about_view(request):
    return render(request, 'about.html')