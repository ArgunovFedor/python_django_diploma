from django.shortcuts import render


# Create your views here.

def cart_view(request):
    return render(request, 'goods/cart.html')


def catalog_view(request):
    return render(request, 'goods/catalog.html')


def payment_view(request):
    return render(request, 'goods/payment.html')


def payment_someone_view(request):
    return render(request, 'goods/paymentsomeone.html')


def product_view(request):
    return render(request, 'goods/product.html')


def progress_payment_view(request):
    return render(request, 'goods/progressPayment.html')


def sale_view(request):
    return render(request, 'goods/sale.html')


def history_order_view(request):
    return render(request, 'goods/historyorder.html')


def one_order_view(request):
    return render(request, 'goods/oneorder.html')


def order_view(request):
    return render(request, 'order.html')
