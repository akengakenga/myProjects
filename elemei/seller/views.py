from django.shortcuts import render,redirect
from order import models
from django.forms import Form,fields,widgets
# Create your views here.

def to_main(request):
    return render(request,'main.html')
#跳转到登录页面
def to_seller_login(request):
    return render(request,'seller_login.html')

#跳转到注册页面
def to_seller_regist(request):
    return render(request,'seller_register.html')
#注销
def seller_logout(request):
    del request.session['seller_id']
    return render(request,'seller_login.html')

#注册页面
def seller_regist(request):
    name=request.POST.get('name')
    pwd=request.POST.get('pwd')
    rpwd=request.POST.get('rpwd')
    if rpwd==pwd:
        models.Sellers.objects.create(seller_name=name,seller_password=pwd)
        return render(request,'seller_login.html')

#登录页面
def login(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    seller=models.Sellers.objects.filter(seller_name=name,seller_password=pwd).values("seller_id","seller_name","seller_password")
    if seller:
        request.session['seller_id']=seller[0]['seller_id']
        seller_info = request.session.get("seller_id")
        nid = seller_info
        print('nid'*10,nid)
        obj = models.Sellers.objects.filter(seller_id=nid).first()
        return render(request,'seller_intro.html',{'obj':obj})
    else:
        return redirect('/to_seller_login/')

#跳转到商家首页
def return_seller(request):
    nid = request.session.get("seller_id")
    obj = models.Sellers.objects.filter(seller_id=nid).first()
    return render(request,'seller_intro.html',{'obj':obj})

#跳转到商家信息模块
def to_seller_detail(request):
    if request.method=='GET':

        if request.session.get("seller_id"):
            nid = request.session.get("seller_id")
            obj = models.Sellers.objects.filter(seller_id=nid).first()
            return render(request, 'seller_detail.html', {'obj': obj})
        else:
            pass

#商家信息FORM
class SellerForm(Form):
    seller_name=fields.CharField(label='商家名')
    seller_password=fields.CharField(label='密码')
    seller_image=fields.ImageField(label='商家头像')
    seller_start=fields.CharField(label='开店时间')
    seller_end=fields.CharField(label='打样时间')
    type_id=fields.IntegerField(
        widget=widgets.Select(choices=models.Types.objects.values_list('type_id', 'type_name')),
        label='主营类型'
    )

#编辑商家个人信息
def update_seller(request):
    if request.method=='GET':
        # nid=request.GET.get('id')
        nid = request.session.get("seller_id")
        row=models.Sellers.objects.filter(seller_id=nid).values('seller_name','seller_password','seller_image','seller_start','seller_end','seller_regist_time','seller_status','type_id').first()
        obj=SellerForm(initial=row)
        return render(request,'update_seller.html',{'obj':obj})
    else:
        img=request.FILES
        print(img)
        obj=SellerForm(data=request.POST,files=request.FILES)
        print(obj.__dict__)
        if obj.is_valid():
            nid=request.session.get("seller_id")
            models.Sellers.objects.filter(seller_id=nid).update(**obj.cleaned_data)
            seller_obj=models.Sellers.objects.filter(seller_id=nid).first()
            print("sadas",seller_obj)
            seller_obj.seller_image=obj.cleaned_data.get("seller_image")
            seller_obj.save()
            return redirect('/to_seller_detail/')
        else:
            print(obj.errors)
        return render(request,'update_seller.html',{'obj':obj})

#跳转到商家商品模块
def to_seller(request):
        nid = request.session.get("seller_id")
        obj = models.Goods.objects.filter(seller_id=nid,goods_status=1)
        obj1 = models.Sellers.objects.filter(seller_id=nid).first()
        return render(request,'seller.html',{'obj':obj,'obj1':obj1})

#商品信息FORM
class GoodsForm(Form):
    goods_image = fields.ImageField(label='商品头像')
    goods_name = fields.CharField(label='商品名称')
    goods_number = fields.IntegerField(label='商品数量')
    goods_price = fields.DecimalField(label='商品价格')
    goods_discount = fields.DecimalField(label='商品折扣')
    goods_description = fields.CharField(label='商品描述')

#商品上架
def add_goods(request):
    if request.method=='GET':
        obj=GoodsForm()
        return render(request,'goods_add.html',{'obj':obj})
    else:
        obj=GoodsForm(data=request.POST,files=request.FILES)
        if obj.is_valid():
            seller_id = request.session.get('seller_id')
            print('sellerid:',seller_id)
            goods_image = obj.cleaned_data['goods_image']
            goods_name = obj.cleaned_data['goods_name']
            goods_number = obj.cleaned_data['goods_number']
            goods_price = obj.cleaned_data['goods_price']
            goods_discount = obj.cleaned_data['goods_discount']
            goods_description = obj.cleaned_data['goods_description']
            models.Goods.objects.create(
                seller_id = seller_id,
                goods_image = goods_image,
                goods_name =goods_name,
                goods_price = goods_price,
                goods_number= goods_number,
                goods_discount =goods_discount,
                goods_description =goods_description
            )
            return redirect('/to_seller/')
        else:
            print(obj.errors)
            return redirect('/add_goods/')
#编辑商品
def update_goods(request):
    if request.method=='GET':
        nid = request.GET.get('nid')
        print(nid)
        request.session['good_id']=nid
        print('session',request.session['good_id'])
        row=models.Goods.objects.filter(goods_id=nid).values('goods_id','goods_image','goods_name','goods_price','goods_number','goods_discount','goods_description','goods_status','seller_id').first()
        obj=GoodsForm(initial=row)
        return render(request,'goods_update.html',{'obj':obj})
    else:
        obj=GoodsForm(data=request.POST,files=request.FILES)
        if obj.is_valid():
            nid = request.session['good_id']
            print("112",nid)
            models.Goods.objects.filter(goods_id=nid).update(**obj.cleaned_data)
            goods_obj=models.Goods.objects.filter(goods_id=nid).first()
            goods_obj.goods_image=obj.cleaned_data.get("goods_image")
            goods_obj.save()
            return redirect('/to_seller/')
        else:
            print(obj.errors)
        return render(request,'goods_update.html',{'obj':obj})

#商品下架
def del_goods(request):
    if request.method=='GET':
        nid=request.GET.get('nid')
        models.Goods.objects.filter(goods_id=nid).update(goods_status=0)
        return redirect('/to_seller/')

#查看商家订单信息
def show_seller_order(request):
    nid = request.session.get("seller_id")
    print(nid)
    obj=models.Orders.objects.filter(seller_id=nid).all()
    money_count=0
    num_count=0
    for row in obj:
        num_count+=1
        money_count+=row.order_money
    print(num_count)
    print(money_count)
    return render(request,'seller_order.html',{'num_count':num_count,'money_count':money_count,'obj':obj})








