"""elemei URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from order import views as orderview
from django.views import static
from shop import views as shopview
from seller import views as sellerview
from users import views as userview
from delivery import views as deliveryview
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns = [
    path('admin/', admin.site.urls),
    path('toindex/',orderview.toindex),
    path('selectbytype/',orderview.selectbytype),
    path('selectbyname/',orderview.selectbyname),


    #shop
    re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': os.path.join(BASE_DIR, 'static')}),
    path('shop_list/', shopview.shop_list),
    path('shop_brand/', shopview.shop_brand),
    path('shop_comment/', shopview.shop_comment),
    path('shop_intro/', shopview.shop_intro),
    path('shop_order/', shopview.shop_order),
    path('shop_detail/', shopview.shop_detail),
    path('get_goods_list/', shopview.get_goods_list),
    path('createorder/', shopview.createorder),


    # seller
    path('to_seller_login/',sellerview.to_seller_login),
    path('seller_login/',sellerview.login),
    path('to_main/',sellerview.to_main),
    path('',sellerview.to_main),
    path('seller_logout/',sellerview.seller_logout),
    path('to_seller_regist/', sellerview.to_seller_regist),
    path('seller_regist/', sellerview.seller_regist),
    path('to_seller_detail/',sellerview.to_seller_detail),
    path('update_seller/',sellerview.update_seller),
    path('return_seller/',sellerview.return_seller),
    path('to_seller/',sellerview.to_seller),
    path('add_goods/',sellerview.add_goods),
    path('update_goods/',sellerview.update_goods),
    path('del_goods/',sellerview.del_goods),
    path('show_seller_order/',sellerview.show_seller_order),

    #跳转登录页面
    path('to_user_login/',userview.tologin),
    path('user_login/',userview.login),
    path('user_order/',userview.user_order),
    path('delete_user_order/',userview.delete_user_order),
    path('user_order_detail/',userview.user_order_detail),
    #跳转注册页面
    path('toreg/',userview.toreg),
    #跳转首页
    path('toindex/',userview.toindex),
    path('reg/',userview.reg),
    #查看用户信息界面
    path('show/',userview.show),
    #修改用户页面
    path('update/',userview.update),
    path('delete_address/',userview.deleta_address),
    path('add_address/',userview.add_address),
    path('update_address/',userview.update_address),
    path('user_logout/',userview.user_logout),

    path('delivery_login/', deliveryview.login),
    path('delivery_logout/', deliveryview.logout),
    path('delivery_toregister/', deliveryview.toregister),
    path('delivery_register/', deliveryview.register),
    path('delivery_inf/', deliveryview.delivery_inf),
    path('delivery_order/', deliveryview.delivery_order),
    path('delivery_order_detail/', deliveryview.delivery_order_detail),
    path('editdelivery/', deliveryview.editdelivery),
    path('confirm_order/', deliveryview.confirm_order),
]
