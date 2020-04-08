from django.shortcuts import render
from logManager.utils.md5 import md5
from django.http import JsonResponse

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from .models import *
from .utils.serializes import *

# Create your views here.
class Login(APIView):
    authentication_classes = []  # 取消login界面的token认证

    def post(self,request,*args,**kwargs):
        print(1)
        ret = {'code':'1000','msg':None}
        user_info = request.data
        print(user_info)
        # try:
        print(user_info,type(user_info))
        print(user_info['usertype'])
        if user_info['usertype'] == 1:
            user1 = Admins.objects.filter(admin_name=user_info['username'],admin_password=user_info['password']).first()
            user2= Admins.objects.filter(admin_phone=user_info['username'], admin_password=user_info['password']).first()
            if user1:
                user = user1
            else:
                if user2:
                    user = user2
                else:user = None
            if not user:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误！'
            else:
                token = md5(user.admin_name)
                AdminToken.objects.update_or_create(user = user,defaults={'token':token})
                ret['code'] = 1002
                ret['msg'] = '登录成功！'
                user_info = AdminSerializer(instance=user,many=False)  # 将admin对象序列化
                ret['user_info'] = user_info.data
                ret['token'] = token
                # request.session['user_id'] = user.admin_id
                # request.session.set_expiry(60*60*24)
                # print('11111',request.session.get('user_id'))
                # data = json.dumps(ret, ensure_ascii=False)
                # resp = Response(data)
                # resp.set_signed_cookie('user_id', user.admin_id, salt='加密盐',max_age=60*60*24)
        elif user_info['usertype'] == 2:
            user1 = Chargers.objects.filter(charger_name=user_info['username'],
                                            charger_password=user_info['password']).first()
            user2 = Students.objects.filter(student_phone=user_info['username'],
                                            student_password=user_info['password']).first()
            if user1:
                user = user1
            else:
                if user2:
                    user = user2
                else:user = None
            if not user:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误！'
                ret['user']['user_info'] = user
            else:
                token = md5(user.charger_name)
                ChargeToken.objects.update_or_create(user = user,defaults={'token':token})
                ret['code'] = 1002
                ret['msg'] = '登录成功！'
                user_info = ChargerSerializer(instance=user, many=False)  # 将admin对象序列化
                ret['user_info'] = user_info.data
                ret['token'] = token
        else:
            user1 = Students.objects.filter(student_no=user_info['username'],
                                            student_password=user_info['password']).first()
            user2 = Students.objects.filter(student_phone=user_info['username'],student_password=user_info['password']).first()
            if user1:
                user = user1
            else:
                if user2:
                    user = user2
                else:user = None
            if not user:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误！'
            else:
                token = md5(user.student_no)
                print(user)
                StudentToken.objects.update_or_create(user=user, defaults={'token': token})
                ret['code'] = 1002
                ret['msg'] = '登录成功！'
                user_info = StudentSerializer(instance=user, many=False)  # 将admin对象序列化
                ret['user_info'] = user_info.data
                ret['token'] = token
        # except Exception as e:
        #     print(e)
        #     ret['code'] = 1003
        #     ret['msg'] = '未知错误!'

        print(ret)
        return Response(ret)


class GetCheckCode(APIView):
    authentication_classes = []
    def get(self, request, *args, **kwargs):
        print(request._request.GET.get('phone'))