from django.contrib import admin

from app_goods.models import Shop, Good, Item, ShoppingCart, Order, Category, Review, ShoppingCardItemLog


# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class GoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'price', 'count']
    list_select_related = ['good' ]
    readonly_fields = ("created_at", "updated_at")



class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at']
class ShoppingCartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'item', 'count']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'updated_at']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'author']
    readonly_fields = ("created_at", "updated_at")

class ShoppingCartLogItemAdmin(admin.ModelAdmin):
    list_display = ['id']
    readonly_fields = ("created_at", "updated_at")

admin.site.register(Shop, ShopAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(ShoppingCardItemLog, ShoppingCartLogItemAdmin)