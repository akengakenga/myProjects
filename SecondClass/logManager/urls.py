from django.urls import path,re_path,include
from . import views
app_name = 'logManager'

urlpatterns = [
    re_path(r'^api/v1/login/$',views.Login.as_view()),#登录
    re_path(r'^api/v1/getcheckcode',views.GetCheckCode.as_view()),#获取验证码
]