from django.urls import re_path
from . import views

app_name = 'ward'

urlpatterns = [
    re_path(r'^addward/$',views.addward,name = 'addward'),  # 添加病房
    re_path(r'^showward/$',views.showward,name = 'showward'),  # 病房列表
    re_path(r'^aboutward/(\d+)/$',views.aboutward,name = 'aboutward'),  # 病房详细信息
    re_path(r'^outward/(\d+)/$',views.outward,name = 'outward'),  # 病人出院
    re_path(r'^inward/(\d+)/$',views.inward,name = 'inward'),  # 病人住院
    re_path(r'^roomtypeajax/$',views.roomtypeajax,name = 'roomtypeajax'),  # 病房类型-->病房下拉框二级联动 ajax
    re_path(r'^roomajax/$',views.roomajax,name = 'roomajax'),  # 病房-->病床下拉框二级联动 ajax

]