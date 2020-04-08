from django.urls import re_path
from . import views

app_name = 'doctor'

urlpatterns = [
    re_path(r'^showdoctor/$',views.showdoctor,name = 'showdoctor'),  # 添医列表
    re_path(r'^doctordetail/(\d+)/$',views.doctordetail,name = 'doctordetail'),  # 医生详情
    re_path(r'^adddoctor/$',views.adddoctor,name = 'adddoctor'),  # 添加医生
    re_path(r'^updatedoctor/(\d+)/$',views.updatedoctor,name = 'updatedoctor'),  # 修改医生信息
    re_path(r'^deletedoctor/(\w+)/$',views.deletedoctor,name = 'deletedoctor'),  # 删除医生
]