from django.shortcuts import render,redirect
from order import models
from order.forms import UserForm

#跳转登录页面
def tologin(request):
    return render(request, 'user_login.html')
def user_logout(request):
    del request.session['user_id']
    return render(request,'main.html')
#用户登录方法
def login(request):
    username= request.POST.get('username')
    userpwd = request.POST.get('userpwd')
    user=models.Users.objects.filter(user_name=username,user_password=userpwd).first()
    msg = '账号或密码错误请重新登录'
    if user:
        request.session['user_id']=user.user_id
        sellers = models.Sellers.objects.all()
        types = models.Types.objects.all()

        return render(request, 'shop_list.html', {'user':user,'sellers': sellers, 'types': types, 'id': '0'})
    else:
        return render(request, 'user_login.html', {'msg':msg})

#跳转注册页面
def toreg(request):
    return render(request,'register.html')

#用户注册方法
def reg(request):
    userimg = request.POST.get('userimg')
    print(userimg)
    username = request.POST.get('username')
    print(username)
    userpwd = request.POST.get('userpwd')
    print(userpwd)
    rpwd = request.POST.get('rpwd')
    print(rpwd)
    userppwd = request.POST.get('userppwd')
    print(userppwd)
    usertel = request.POST.get('usertel')
    print(usertel)
    if userpwd == rpwd:
        user = models.Users(userimg=userimg,username=username,userpwd=userpwd,userppwd=userppwd,usertel=usertel)
        user.save()
        return render(request, 'user_login.html')
    else:
        msg = "两次密码不一致，请重新输入"
        return render(request,'register.html',{'msg':msg})

#跳转首页
def toindex(request):
    user_info = request.session.get('userid')
    userid = user_info["userid"]
    obj = models.Users.objects.filter(userid=userid).first()
    return render(request, 'user_list.html', {'obj': obj})

#查看用户信息
def show(request):
    if request.method == 'GET':
        userid = request.session.get("user_id")
        user = models.Users.objects.filter(user_id=userid).first()
        obj = models.Users.objects.filter(user_id=userid).first()
        address = models.Address.objects.filter(user_id=userid,address_status=1)
        return render(request, 'user_show.html', {'obj': obj,'user':user,'address':address})


#修改用户信息
def update(request):
    if request.method == "GET":
        uid = request.session.get('user_id')
        print('uid',uid)
        user = models.Users.objects.filter(user_id = uid).first()
        uform = UserForm(instance = user)
        return render(request,'user_update.html',{'uform':uform,'user':user})
    else:
        uid = request.session.get('user_id')
        user = models.Users.objects.filter(user_id=uid).first()
        form = UserForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            sellers = models.Sellers.objects.all()
            types = models.Types.objects.all()
            return render(request, 'shop_list.html', {'user': user, 'sellers': sellers, 'types': types, 'id': '0'})
        else:
            return render(request,'user_update.html',{'uform':form})
def deleta_address(request):
    address_id =request.GET.get('address_id')
    print(address_id)
    models.Address.objects.filter(address_id=int(address_id)).update(address_status=0)
    return redirect('/show/')

def add_address(request):
    if request.method =='GET':
        userid = request.session.get("user_id")
        user = models.Users.objects.filter(user_id=userid).first()
        return render(request,'add_address.html',{'user':user})
    else:
        userid = request.session.get("user_id")
        address_id = request.POST.get('address_id')
        address_content = request.POST.get('address_content')
        address = models.Address.objects.create(address_content=address_content,user_id=userid)

        return redirect('/show/')

def update_address(request):
    if request.method =='GET':
        userid = request.session.get("user_id")
        user = models.Users.objects.filter(user_id=userid).first()
        address_id = request.GET.get('address_id')
        address = models.Address.objects.filter(address_id=address_id).first()
        return render(request,'update_address.html',{'user':user,'address':address})
    else:
        address_id = request.POST.get('address_id')
        address_content = request.POST.get('address_content')
        address = models.Address.objects.filter(address_id=address_id).update(address_content=address_content)
        return redirect('/show/')

def user_order(request):
    userid = request.session.get("user_id")
    user = models.Users.objects.filter(user_id=userid).first()
    orders = models.Orders.objects.filter(address__user_id=userid,order_status__in=[1,2])
    return render(request,'user_order.html',{'orders':orders,'user':user})
def delete_user_order(request):
    order_id = request.GET.get('order_id')
    models.Orders.objects.filter(order_id=int(order_id)).update(order_status=0)
    return redirect('/user_order/')
def user_order_detail(request):
    if request.method =='GET':
        userid = request.session.get("user_id")
        user = models.Users.objects.filter(user_id=userid).first()
        order_id = request.GET.get('order_id')
        order = models.Orders.objects.filter(order_id=order_id).first()
        print(order.__dict__)
        order_detail = models.Orderdetails.objects.filter(order_id=order_id)
        return render(request,'user_order_detail.html',{'user':user,'order':order,'order_detail':order_detail})
