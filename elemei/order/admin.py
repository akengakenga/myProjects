from django.contrib import admin
from order.models import *
# Register your models here.
class SellersAdmin(admin.ModelAdmin):
    list_select_related = True
    list_per_page = 10
    list_display = ['seller_id','seller_name','seller_image']
    def __str__(self):
        return Sellers.seller_name
class GoodsAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ['goods_name','goods_number','goods_price','seller_id']
    list_per_page = 10

class OrdersAdmin(admin.ModelAdmin):
    list_select_related = True
    list_per_page = 10

class OrderdetailsAdmin(admin.ModelAdmin):
    list_select_related = True
    list_per_page = 10

class TypesAdmin(admin.ModelAdmin):
    list_select_related = True
    list_per_page = 10



# Register your models here.
admin.site.site_header = '后台管理'
admin.site.site_title = '后台管理'
admin.site.register(Sellers, SellersAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Orderdetails, OrderdetailsAdmin)
admin.site.register(Types, TypesAdmin)