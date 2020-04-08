from django.urls import re_path
from . import views

app_name = 'president'

urlpatterns = [
    re_path(r'^login/$',views.login,name = 'login'),  # 登录
    re_path(r'^logout/$',views.logout,name = 'logout'),  # 登出
    re_path(r'^toindex/$',views.toindex,name = 'toindex'),  # 跳转到信息统计页面
]