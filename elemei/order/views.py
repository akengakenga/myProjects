from django.shortcuts import render
from .models import *
# Create your views here.
def toindex(request):
    sellers = Sellers.objects.all()
    types = Types.objects.all()
    user_id = request.session.get('user_id')
    user = Users.objects.filter(user_id=user_id).first()
    return render(request,'shop_list.html',{'user':user,'sellers':sellers,'types':types,'id':'0'})
def selectbytype(request):
    id = request.GET.get('id','')
    print(id,type(id))
    if int(id) == 0:
        print('id=0')
        sellers = Sellers.objects.all()
    else:
        print('id!=0')
        sellers = Sellers.objects.filter(type_id=id)
    types = Types.objects.all()
    print('id:',id,type(id))
    typeid = Types.objects.all().first()
    print('typeid:',typeid,type(typeid.type_id))
    print(len(sellers))
    return render(request,'shop_list.html',{'sellers':sellers,'types':types,'id':int(id)})
def selectbyname(request):
    sname = request.POST.get('sname')
    sellers = Sellers.objects.filter(seller_name__contains=sname)
    types = Types.objects.all()
    return render(request, 'shop_list.html', {'sellers': sellers, 'types': types, 'id': '0','sname':sname})