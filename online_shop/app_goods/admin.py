from django.contrib import admin
from app_goods.models import Shop, Good, Item, ShoppingCart, Order


# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class GoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'price', 'count']


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'count']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(Shop, ShopAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(Order, OrderAdmin)
