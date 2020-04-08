from django.shortcuts import render,redirect,reverse
from .models import *
from patient.models import *
from doctor.models import *
from patient.models import *
from treat.models import *
from ward.models import *

# Create your views here.


def toindex(request):
    """
    跳转到信息统计页面
    :param request:
    :return:
    """
    user_id = request.session.get('user_id')
    president = President.objects.get(pk=user_id)
    doctor = Doctor.objects.all().count()
    patient = Patient.objects.all().count()
    treat = Treat.objects.all().count()
    cure = Treat.objects.filter(treat_status=0).count()
    room = Room.objects.all().count()
    bed = RoomBed.objects.all().count()

    return render(request,'index.html',locals())


def login(request):
    """
    登录
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        president = President.objects.filter(pre_name=username,pre_password=password).first()
        patient = Patient.objects.filter(p_name=username,p_password=password).first()
        doctor = Doctor.objects.filter(doc_name=username,doc_password=password).first()
        if president :  # 根据用户类型以此匹配
            request.session['user_id'] = president.pre_id  # 用户id
            request.session['user_name'] = president.pre_name  # 用户名
            request.session['user_type'] = president.user_type.type_id  # 用户类型
            request.session.set_expiry(0)  # 在浏览器关闭时删除cookie
            return redirect(reverse('president:toindex'))
        else:
            if patient:
                print(1)
                request.session['user_id'] = patient.p_id
                request.session['user_name'] = patient.p_name
                request.session['user_type'] = patient.user_type.type_id
                request.session.set_expiry(0)  # 在浏览器关闭时删除cookie
                return redirect(reverse('president:toindex'))
            else:
                if doctor:
                    request.session['user_id'] = doctor.doc_id
                    request.session['user_name'] = doctor.doc_name
                    request.session['user_type'] = doctor.user_type.type_id
                    request.session.set_expiry(0)  # 在浏览器关闭时删除cookie
                    return redirect(reverse('president:toindex'))
        return render(request, 'login.html', {'msg': '用户名或密码错误'})


def logout(request):
    """
    登出
    :param request:
    :return:
    """
    del request.session['user_id']  # 删除session
    del request.session['user_name']
    del request.session['user_type']
    return render(request,'login.html')