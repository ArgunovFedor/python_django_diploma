from django.urls import path
from app_goods.views import order_view, one_order_view, history_order_view, CatalogListView, payment_someone_view, \
    progress_payment_view, sale_view, cart_view, payment_view, ProductDetailView, add_cart_item_view, \
    delete_cart_item_view

urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('payment/', payment_view, name='payment'),
    path('paymentsomeone/', payment_someone_view, name='payment-someone'),
    path('progressPayment/', progress_payment_view, name='progress-payment'),
    path('sale/', sale_view, name='sale'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('historyorder/', history_order_view, name='history-order'),
    path('oneorder/', one_order_view, name='one-order'),
    path('order/', order_view, name='order'),
    path('order/<int:pk>/', order_view, name='order'),
    path('addCartItem/', add_cart_item_view, name='add-cart-item'),
    path('deleteCartItem/<int:product_id>/', delete_cart_item_view, name='delete_cart_item'),
    path('viewingHistory/', history_order_view, name='viewing-history')
]
