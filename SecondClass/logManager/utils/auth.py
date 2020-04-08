from rest_framework import exceptions
from rest_framework.authentication import BasicAuthentication
from logManager.models import *


class Authtication(BasicAuthentication):
    """用户认证"""

    def authenticate(self,request):
        # print(request.META)
        # token = request.META.GET('HTTP_AUTHORIZATION')
        # print(token)
        token1 = request._request.POST.get('token')
        token1 = request.data.get('token')
        token1 = request.POST.get('token')

        token2 = request._request.GET.get('token')



        if token1:
            token = token1
        else:
            token = token2


        print(token)
        # token = request.META.get('HTTP_AUTHORIZATION')
        token_obj1 = AdminToken.objects.filter(token=token).first()
        token_obj2 = ChargeToken.objects.filter(token=token).first()
        token_obj3 = StudentToken.objects.filter(token=token).first()

        if not token_obj1:
            if not token_obj2:
                if not token_obj3:
                    print('shibai')
                    raise exceptions.AuthenticationFailed('用户认证失败')
                else:
                    return (token_obj3.user,token_obj3)
            else:
                return (token_obj2.user,token_obj1)
        else:
            return (token_obj1.user, token_obj1)