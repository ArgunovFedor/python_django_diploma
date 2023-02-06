from app_goods.models import ShoppingCart


def try_parse_int(text):
    try:
        result = int(text)
        if result > 0:
            return result
        else:
            return 1
    except:
        return 1


def get_user_cart_aggregations_item(user_id: int):
    """
    Возвращает элемент с аггрегирующими полями типа общая сумма, общее количество.
    Если у пользователя нету корзины, то возвращает None
    """
    # Берем из базы корзину пользователя
    user_cart = ShoppingCart.objects.filter(user_id=user_id).select_related('item').all()

    # можно было использовать джанго аггрегации, но такой подход мне понятнее
    if user_cart is not None:
        cart_items = {
            # общее количество товаров
            'count': sum([cart.count for cart in user_cart]),
            # общая сумма
            'sum': sum([cart.item.price * cart.count for cart in user_cart])
        }
        return cart_items
    return None
