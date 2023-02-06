from app_goods.models import Category
from app_goods.utils import get_user_cart_aggregations_item


def categories(request):
    # TODO: Придумать как захешировать...
    cart_items = get_user_cart_aggregations_item(request.user.id)
    return {
        'cart_items': cart_items,
        'categories': Category.objects.all()
    }
