from django.urls import path,re_path,include
from . import views
app_name = 'activities'

urlpatterns = [
    #系统管理员
    #活动
    re_path(r'^api/v1/activitytype$',views.ActivityType.as_view()),  # 添加活动类型
    re_path(r'^api/v1/activitytype(?P<token>\w+)$',views.ActivityType.as_view()),  # 查询活动类型
    re_path(r'^api/v1/getchargers$',views.GetChargers.as_view()),  # 添加活动类型
    re_path(r'^api/v1/updateactivitytype$',views.UpdateActivityType.as_view()),  # 修改活动类型
    re_path(r'^api/v1/delactivitytype$',views.DelActivityType.as_view()),  # 删除活动类型
    re_path(r'^api/v1/addactivity$',views.AddActivity.as_view()),  # 添加活动类型
    re_path(r'^api/v1/myactivity',views.MyActivity.as_view()),  # 活动列表
    re_path(r'^api/v1/updateactivity',views.UpdateActivity.as_view()),  # 活动列表
    re_path(r'^api/v1/delactivity$',views.DelActivity.as_view()),  # 删除活动
    #负责人
    re_path(r'api/v1/schools$',views.SchoolList.as_view()), #所有学校
    re_path(r'api/v1/addcharger$',views.AddCharger.as_view()), #添加负责人
    re_path(r'api/v1/allchargers$',views.ChargerList.as_view()), #所有负责人
    re_path(r'api/v1/updatecharger$',views.UpdateCharger.as_view()), #修改负责人
    re_path(r'api/v1/delcharger$',views.DelCharger.as_view()), #删除负责人
    #公告
    re_path(r'api/v1/addnotice$',views.AddNotice.as_view()), #添加公告
    re_path(r'api/v1/allnotices$',views.AllNotices.as_view()), #添加公告
    re_path(r'api/v1/updatenotice$',views.UpdateNotice.as_view()), #添加公告
    re_path(r'api/v1/delnotice$',views.DelNotice.as_view()), #添加公告
    #学生管理
    re_path(r'api/v1/classinf$',views.ClassInf.as_view()),  # 获取学校学院专业班级
    re_path(r'api/v1/schoolchange$',views.SchoolChange.as_view()),  # 学校联动切换
    re_path(r'api/v1/departmentchange$',views.DepartmentChange.as_view()),  # 学院联动切换
    re_path(r'api/v1/majorchange$',views.MajorChange.as_view()),  # 专业联动切换
    re_path(r'api/v1/classchange$',views.ClassChange.as_view()),  # 班级联动切换
    re_path(r'api/v1/addstudent$',views.AddStudent.as_view()),  # 添加学生
    re_path(r'api/v1/studentclass$',views.StudentClass.as_view()),  # 修改学生页面相关信息
    re_path(r'api/v1/changestudent$',views.ChangeStudent.as_view()),  # 修改学生
    re_path(r'api/v1/updatestudent$',views.UpdateStudent.as_view()),  # 修改学生信息
    re_path(r'api/v1/delstudent$',views.DeleteStudent.as_view()),   # 删除学生



    #学生
    re_path(r'api/v1/studentactivity$',views.StuedntActivityId.as_view()),  # 学生参加活动列表
    re_path(r'api/v1/attendactivity$',views.AllStuedntActivity.as_view()),  # 所有学生参加活动
    re_path(r'api/v1/regActivity$',views.RegActivity.as_view()),  # 报名活动
    re_path(r'api/v1/cancelActivity$',views.CancelActivity.as_view()),  # 报名活动
    re_path(r'api/v1/studentinfo$',views.StuedntInfo.as_view()),  # 学生信息
    re_path(r'api/v1/creditinfo$',views.CreditInfo.as_view()),  # 学分信息
    re_path(r'api/v1/downloadcredit',views.DownloadCredit.as_view()),  # 下载学分详情

    #负责人
    re_path(r'api/v1/activitydetail$',views.ActivityDetail.as_view()),  # 活动详情
    re_path(r'api/v1/signin$',views.SignIn.as_view()),  # 活动签到
    re_path(r'api/v1/signout$',views.SignOut.as_view()),  # 活动签退
    re_path(r'api/v1/chargerinfo$',views.ChargerInfo.as_view()),  # 负责人信息
    re_path(r'api/v1/giveCredit$',views.GiveCredit.as_view()),  # 负责人信息
]