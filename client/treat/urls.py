from django.urls import re_path
from . import views

app_name = 'treat'

urlpatterns = [
    re_path(r'^addtreat/$',views.addtreat,name = 'addtreat'),  # 添加出诊信息
    re_path(r'^addtreatdetail/$',views.addtreatdetail,name = 'addtreatdetail'),  # 出诊类型-->病人，医生 下拉框二级联动 ajax
    re_path(r'^showtreat/$',views.showtreat,name = 'showtreat'),  # 出诊信息列表
    re_path(r'^updatetreat/(\d+)/$',views.updatetreat,name = 'updatetreat'),  # 修改出诊信息
    re_path(r'^deletetreat/(\w+)/$',views.deletetreat,name = 'deletetreat'),  # 删除出诊信息
]