from django.shortcuts import render,redirect,HttpResponse
from order import models
from order.models import Deliveries,Orders,Orderdetails,Sellers,Goods
import os
# Create your views here.
#登录功能
def login(request):
   if request.method =="GET":
        return render(request,'delivery_login.html')
   else:
        delivery_name = request.POST.get('delivery_name')
        delivery_password = request.POST.get("delivery_password")
        delivery = models.Deliveries.objects.filter(delivery_name=delivery_name,delivery_password=delivery_password).first()
        delivery_id = delivery.delivery_id
        request.session['delivery_id']=delivery_id
        if delivery:
            return redirect('/delivery_order/')
        else:
            return render(request,'delivery_login.html',{'msg':"账号或密码错误重新登录"})
def delivery_order(request):
    delivery_id=request.session['delivery_id']
    delivery = models.Deliveries.objects.filter(delivery_id=delivery_id).first()
    user = models.Users.objects.all()
    orders = models.Orders.objects.filter(delivery_id=delivery_id)
    num_count = 0
    for row in orders:
        num_count += 1
    money_count = num_count * 2
    return render(request, 'delivery.html',{'user': user, 'delivery': delivery, 'orders': orders, 'num_count': num_count,'money_count': money_count})


#退出
def logout(request):
    del request.session['delivery_id']
    return render(request, 'main.html')
#注册
def register(request):
    delivery_name = request.POST.get('delivery_name')
    delivery_password = request.POST.get('delivery_password')
    delivery_repassword = request.POST.get('delivery_repassword')
    delivery_mobile = request.POST.get('delivery_mobile')
    delivert_image = request.POST.get('delivert_image')
    if delivery_password == delivery_repassword:
        delivery = Deliveries(delivery_name=delivery_name,delivery_password=delivery_password,delivery_mobile=delivery_mobile,delivert_image =delivert_image)
        delivery.save()
        return render(request,'delivery_login.html',{'delivery':delivery})
    else:
        return render(request, 'delivery_register.html', {'msg': "两次输入密码不一致"})

def delivery_order_detail(request):
    if request.method == 'GET':
        delivery_id = request.session.get("delivery_id")
        delivery = models.Deliveries.objects.filter(delivery_id=delivery_id).first()
        order_id = request.GET.get('order_id')
        order = models.Orders.objects.filter(order_id=order_id).first()
        print(order.__dict__)
        order_detail = models.Orderdetails.objects.filter(order_id=order_id)
        return render(request, 'delivery_order_detail.html', {'delivery': delivery, 'order': order, 'order_detail': order_detail})
def confirm_order(request):
    order_id = request.GET.get('order_id')
    models.Orders.objects.filter(order_id=order_id).update(order_status = 2)
    return redirect('/delivery_order/')

def delivery_inf(request):
    delivery_id = request.session.get("delivery_id")
    delivery = models.Deliveries.objects.filter(delivery_id=delivery_id).first()
    return render(request,'delivery_inf.html',{'delivery':delivery})
#跳转到注册页面
def toregister(request):
    return render(request,'delivery_register.html')

#修改骑手信息
def editdelivery(request):
    if request.method == "GET":
        delivery_id = request.session.get("delivery_id")
        delivery = models.Deliveries.objects.filter(delivery_id=delivery_id).first()
        return render(request,'editdelivery.html',{'delivery':delivery})
    else:
        delivery_id = request.session['delivery_id']
        delivery_name = request.POST.get('delivery_name')
        delivery_mobile = request.POST.get('delivery_mobile')
        delivery_password = request.POST.get('delivery_password')
        delivery = Deliveries.objects.filter(delivery_id=delivery_id).update(delivery_name=delivery_name,delivery_mobile=delivery_mobile,delivery_password=delivery_password)
        return redirect('/delivery_login/')
#骑手个人信息展示
def delivery(request):
    deliveryinfo=request.session['deliveryinfo']
    delivery_id=deliveryinfo['delivery_id']
    order=models.Orders.objects.filter(delivery_id=delivery_id).all()
    for row in order:
        print(row.order_money)
    return render(request,'delivery.html',{'order':order})

