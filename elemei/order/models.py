from django.db import models
from django.utils import timezone

# Create your models here.
#用户表
class Users(models.Model):
    user_id = models.AutoField(verbose_name='用户id',primary_key=True)
    user_name = models.CharField(verbose_name='用户名',max_length=32)
    user_password = models.CharField(verbose_name='密码',max_length=32)
    user_pay_password = models.CharField(verbose_name='支付密码',max_length=11,null=True)
    user_mobile = models.CharField(verbose_name='手机号',max_length=11)
    user_status = models.IntegerField(verbose_name='用户状态',default=1)
    user_image = models.ImageField(verbose_name='用户头像',upload_to='user/%Y/%m',default='default.jpeg')
    user_face = models.CharField(verbose_name='用户人脸地址',max_length=100,null=True)

#收货地址表
class Address(models.Model):
    address_id = models.AutoField(verbose_name='收货地址id',primary_key=True)
    address_content = models.CharField(verbose_name='收货地址',max_length=100)
    address_status = models.IntegerField(verbose_name='收货地址状态',default=1)
    user = models.ForeignKey(to = Users,to_field='user_id',on_delete=models.CASCADE)

#商家主营类型表
class Types(models.Model):
    type_id = models.AutoField(verbose_name='主营类型id',primary_key=True)
    type_name = models.CharField(verbose_name='主营类型',max_length=100)
    type_status = models.IntegerField(verbose_name='主营类型状态',default=1)
    def __str__(self):
        return self.type_name
#商家表
class Sellers(models.Model):
    seller_id = models.AutoField(verbose_name='商家id', primary_key=True)
    seller_name = models.CharField(verbose_name='商家名称',max_length=100,null=True)
    seller_image = models.ImageField(verbose_name='商家头像',upload_to='seller/%Y/%m',default='default.jpeg')
    seller_password = models.CharField(verbose_name='商家密码',max_length=100,default='123456789')
    seller_start = models.CharField(verbose_name='每日开店时间',max_length=100,default='10')
    seller_nums = models.IntegerField(verbose_name='销量',default=0)
    seller_end = models.CharField(verbose_name='每日打样时间',max_length=100,default='20')
    seller_regist_time = models.DateTimeField(verbose_name='商家注册时间',default=timezone.now)
    seller_status = models.IntegerField(verbose_name='商家状态',default=1)
    type = models.ForeignKey(to = Types,to_field='type_id',on_delete=models.CASCADE,null=True)

#商品表
class Goods(models.Model):
    goods_id = models.AutoField(verbose_name='用户id',primary_key=True)
    goods_name = models.CharField(verbose_name='用户名',max_length=100)
    goods_number = models.IntegerField(verbose_name='商品数量')
    goods_price = models.DecimalField(verbose_name='商品价格',max_digits=10,decimal_places=2)
    goods_discount = models.DecimalField(verbose_name='商品折扣',max_digits=3,decimal_places=2)
    goods_description = models.CharField(verbose_name='商品描述',max_length=100)
    goods_status = models.IntegerField(verbose_name='商品状态',default=1)
    goods_image = models.ImageField(verbose_name='商品图片',upload_to='goods/%Y/%m',default='static/head_images/goods/default.jpeg')
    seller = models.ForeignKey(to = Sellers,to_field='seller_id',on_delete=models.CASCADE)

#骑手表
class Deliveries(models.Model):
    delivery_id = models.AutoField(verbose_name='骑手id',primary_key=True)
    delivery_name = models.CharField(verbose_name='骑手登录名',max_length=100)
    delivery_password = models.CharField(verbose_name='密码',max_length=32)
    delivery_mobile = models.CharField(max_length=13)
    delivert_status = models.IntegerField(verbose_name='骑手id',default=1)
    delivert_image = models.ImageField(verbose_name='骑手头像',upload_to='delivery/%Y/%m',default='default.jpeg')

#订单表
class Orders(models.Model):
    order_id = models.AutoField(verbose_name='id',primary_key=True)
    order_name = models.CharField(verbose_name='订单编号',max_length=100)
    order_money = models.DecimalField(verbose_name='订单金额',max_digits=10,decimal_places=2)
    order_time = models.DateTimeField(verbose_name='下单时间')
    order_reamrk = models.CharField(verbose_name='订单备注',max_length=100,default='')
    order_status = models.IntegerField(verbose_name='订单状态',default=1)
    address = models.ForeignKey(to = Address,to_field='address_id',on_delete=models.CASCADE)
    delivery = models.ForeignKey(to = Deliveries,to_field='delivery_id',on_delete=models.CASCADE)
    seller = models.ForeignKey(to = Sellers,to_field='seller_id',on_delete=models.CASCADE)

class Orderdetails(models.Model):
    detail_id = models.AutoField(verbose_name='订单详情id',primary_key=True)
    order = models.ForeignKey(to = Orders,to_field='order_id',on_delete=models.CASCADE)
    goods = models.ForeignKey(to = Goods,to_field='goods_id',on_delete=models.CASCADE)
    goods_count = models.IntegerField(verbose_name='商品数量')