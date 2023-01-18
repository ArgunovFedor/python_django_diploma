from django.urls import path
from app_goods.views import order_view, one_order_view, history_order_view, catalog_view, payment_someone_view, \
    product_view, progress_payment_view, sale_view, cart_view, payment_view

urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('catalog/', catalog_view, name='catalog'),
    path('payment/', payment_view, name='payment'),
    path('paymentsomeone/', payment_someone_view, name='payment-someone'),
    path('progressPayment/', progress_payment_view, name='progress-payment'),
    path('sale/', sale_view, name='sale'),
    path('product/', product_view, name='product'),
    path('historyorder/', history_order_view, name='history-order'),
    path('oneorder/', one_order_view, name='one-order'),
    path('order/', order_view, name='order'),
]
