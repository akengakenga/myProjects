from django.urls import re_path
from . import views

app_name = 'patient'

urlpatterns = [
    re_path(r'^showpatient/$',views.showpatient,name = 'showpatient'),  # 病人列表
    re_path(r'^patientdetail/(\d+)/$',views.patientdetail,name = 'patientdetail'),  # 病人详情
    re_path(r'^addpatient/$',views.addpatient,name = 'addpatient'),  # 添加病人
    re_path(r'^updatepatient/(\d+)/$',views.updatepatient,name = 'updatepatient'),  # 修改病人信息
    re_path(r'^deletepatient/(\w+)/$',views.deletepatient,name = 'deletepatient'),  # 删除病人
    re_path(r'^patientregister/(\d+)/$',views.patientregister,name = 'patientregister'),  # 病人挂号
]