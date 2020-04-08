from django.shortcuts import render,redirect
# Create your views here.
from django.shortcuts import render,HttpResponse
from order.models import *
from django.http import JsonResponse
import time
import random
# Create your views here.
def shop_list(request):
    return render(request,'shop_list.html')

def shop_brand(request):
    return render(request,'shop_brand.html')

def shop_comment(request):
    return render(request,'shop_comment.html')

def shop_detail(request):
    shop_id = request.GET.get('shop_id')
    seller = Sellers.objects.filter(seller_id=int(shop_id)).first()
    request.session['shop_id'] = shop_id
    print(shop_id,type(shop_id))
    user_id = request.session.get('user_id')
    user = Users.objects.filter(user_id=user_id).first()
    return render(request,'shop_detail.html',{'seller':seller,'user':user})

def shop_intro(request):
    return render(request,'shop_intro.html')

def shop_order(request):
    return render(request,'shop_order.html')

def get_goods_list(request):
    shop_id = request.GET.get('shop_id')
    shop_img = Sellers.objects.filter(seller_id=int(shop_id)).first().seller_image.name
    print('shop_id:',shop_id)
    print(shop_img)
    results = Goods.objects.filter(seller__seller_id=int(shop_id))
    list_all=[]
    for i in results:
        collections={}
        collections['goods_id']=i.goods_id
        collections['goods_name']=i.goods_name
        collections['goods_price']=i.goods_price
        collections['goods_true_price']=round(i.goods_price*i.goods_discount,2)
        collections['goods_image']=i.goods_image.url
        collections['goods_number']=i.goods_number
        list_all.append(collections)
    return JsonResponse({"data":list_all,"shop_img":shop_img})
def createorder(request):
    if request.method=='GET':
        total_price = float(request.GET.get('total_price'))
        print(total_price,type(total_price))
        userid = request.session.get('user_id')
        print(userid)
        sellerid = request.session.get('shop_id')
        print(sellerid)
        ids = request.GET.get('ids')
        list_id = ids.split(',')
        list_id.pop()
        dict_id = {}
        for i in list_id:
            if i not in dict_id:
                dict_id[i] = 1
            else:
                dict_id[i] = dict_id[i]+1
        print(dict_id)
        address = Address.objects.filter(user_id=userid)
        goods = Goods.objects.filter(seller_id=sellerid)
        user_id = request.session.get('user_id')
        user = Users.objects.filter(user_id=user_id).first()
        return render(request,'order.html',{'user':user,'dict_id':dict_id,'goods':goods,'address':address,'total_price':total_price,'seller_id':sellerid})
    else:
        user_id = request.session.get("user_id")
        seller_id = request.session.get("shop_id")
        address_id = request.POST.get("address_id")
        remark = request.POST.get("remark","无")
        goods_id = request.POST.getlist("goods_id")
        goods_count = request.POST.getlist('goods_count')
        goods_price = request.POST.getlist('goods_price')
        goods_tmoney = request.POST.get('goods_tmoney')
        order_name = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        order_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        deliverys = Deliveries.objects.all()
        delivery_list=[]
        for i in deliverys:
            delivery_list.append(i.delivery_id)
        delivery_id = delivery_list[random.randint(0,len(delivery_list)-1)]
        order_name = order_name +'0000'+ str(seller_id) + '0000'+ str(user_id)
        print(order_name)
        order = Orders.objects.create(
            order_name= order_name,
            order_money= goods_tmoney,
            order_time= order_time,
            order_status= 1,
            address_id = address_id,
            delivery_id = delivery_id,
            seller_id= seller_id,
            order_reamrk=remark,
        )

        for i in range(len(goods_id)):
            orderdetail = Orderdetails.objects.create(
                goods_count = goods_count[i],
                goods_id = goods_id[i],
                order_id = order.order_id
            )
        return redirect('/user_order/')