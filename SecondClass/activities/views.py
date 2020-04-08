from django.shortcuts import render
from django.http import HttpResponse,FileResponse
from .models import *
from logManager.models import *
from logManager.utils.serializes import *
from activities.utils.mypaginations import *
from activities.utils.serializes import *
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .utils.mypaginations import MyNumberPagination
import json
import datetime
import pytz
import xlwt
import xlrd
from  xlutils.copy import copy
from logManager.models import *
# Create your views here.

class ActivityType(APIView):
    # authentication_classes = []
    def get(self,request,*args,**kwargs):
        '''获取所有活动类型'''
        ac = ActivityTypes.objects.filter(type_status=1)
        # 创建分页对象
        pg = MyNumberPagination()
        # 获取分页的数据
        # pg_types = pg.paginate_queryset(queryset=ac,request=request,view=self)
        # 序列化
        ret = ActiviyTypeSerializer(instance=ac,many=True)
        return Response(ret.data)

    def post(self,request,*args,**kwargs):
        '''添加活动类型'''
        ret = {'code': '1000', 'msg': None}
        type_info = request.data
        print(type_info)
        # try:
        ActivityTypes.objects.get(pk=2)
        ActivityTypes.objects.create(type_name=type_info['type_name'])
        # except Exception as e:
        #     print(e)
        #     ret['code'] = 1003
        #     ret['msg'] = '未知错误!'
        print(type_info)
        return Response(ret)


class GetChargers(APIView):
    def get(self, request, *args, **kwargs):
        token = request._request.GET.get('token')
        school_id = request._request.GET.get('school')
        school_id = Admins.objects.filter(admintoken__token=token).first().school.school_id
        print(school_id)
        ch = Chargers.objects.filter(charger_status=1,school_id=int(school_id))
        ret = ChargerSerializer(instance=ch, many=True)
        return Response(ret.data)


class UpdateActivityType(APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        print(data)
        type1 = ActivityTypes.objects.get(pk=int(data['type_id']))
        type1.type_name = data['type_name']
        type1.save()
        ret = {'msg':'ok'}
        return Response(json.dumps(ret))


class DelActivityType(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        id = request.data['type_id']
        type1 = ActivityTypes.objects.get(pk=int(id))
        type1.type_status = 0
        type1.save()
        ret = {'msg':'ok'}
        return Response(json.dumps(ret))


class MyActivity(APIView):
    def get(self,request,*args,**kwargs):
        user_type = request._request.GET.get('user_type')
        token = request._request.GET.get('token')
        type_id = request._request.GET.get('type_id')
        activity_status = request._request.GET.get('activity_status')
        now1 = datetime.datetime.now()
        now1 = now1.replace(tzinfo=pytz.timezone('Asia/Shanghai'))
        print(int(activity_status))
        if user_type == '3':  # 判断是否是学生
            school_id = Students.objects.filter(studenttoken__token=token).first().classes.major.department.school_id
            if type_id =='0':  # 判断是否是全部类型
                if activity_status == '4':  # 判断是否是全部状态
                    ac = Activities.objects.filter(creater__school_id = school_id,
                                                   activity_status__in=[1, 2, 3])
                else:
                    ac = Activities.objects.filter(creater__school_id = school_id,
                                                   activity_status = activity_status)
            else:
                if activity_status == '4':  # 判断是否是全部状态
                    ac = Activities.objects.filter(activity_type_id=int(type_id),
                                              activity_status__in=[1, 2, 3],
                                              creater__school_id = school_id,)
                else:
                    ac = Activities.objects.filter(activity_type_id=int(type_id),
                                                   activity_status=int(activity_status),
                                                   creater__school_id = school_id,)
        elif user_type == '2':  # 判断是否是活动负责人
            charger_id = Chargers.objects.filter(chargetoken__token=token).first().charger_id
            if type_id == '0':  # 判断是否是全部类型
                if activity_status == '4':  # 判断是否是全部状态
                    ac = Activities.objects.filter(charger_id=charger_id,
                                                   activity_status__in=[1, 2, 3])
                else:
                    ac = Activities.objects.filter(charger_id=charger_id,
                                                   activity_status=activity_status)
            else:
                if activity_status == '4':  # 判断是否是全部状态
                    ac = Activities.objects.filter(activity_type_id=int(type_id),
                                              activity_status__in=[1, 2, 3],
                                              charger_id=charger_id)
                else:
                    ac = Activities.objects.filter(activity_type_id=int(type_id),
                                                   activity_status=int(activity_status),
                                                   charger_id=charger_id)
        else:  # 系统管理员
            admin_id = Admins.objects.filter(admintoken__token=token).first().admin_id
            if type_id == '0':  # 判断是否是全部类型
                if activity_status == '4':  # 判断是否是全部状态
                    ac = Activities.objects.filter(creater_id=admin_id,
                                                   activity_status__in=[1, 2, 3])
                else:
                    ac = Activities.objects.filter(creater_id=admin_id,
                                                   activity_status=activity_status)
            else:
                if activity_status == '4':  # 判断是否是全部状态
                    ac = Activities.objects.filter(creater_id=admin_id,
                                                   activity_status__in=[1, 2, 3],
                                                   activity_type_id=int(type_id))
                else:
                    ac = Activities.objects.filter(creater_id=admin_id,
                                                   activity_status=int(activity_status),
                                                   activity_type_id=int(type_id))
        # 创建分页对象
        for i in ac:
            start1 = i.activity_start_time
            end1 = i.activity_end_time
            if i.activity_end_time < now1:
                i.activity_status = 3
                i.save()
            else:
                if i.activity_start_time < now1:
                    i.activity_status = 2
                    i.save()
        pg = MyNumberPagination()
        # 获取分页的数据
        pg_types = pg.paginate_queryset(queryset=ac,request=request,view=self)
        # 序列化
        ret = ActiviySerializer(instance=pg_types, many=True)
        return pg.get_paginated_response(ret.data)

class AddActivity(APIView):
    def post(self,request,*args,**kwargs):
        admin1_id = AdminToken.objects.filter(token=request.data['token']).first().user_id
        activity = json.loads(request.data['activity'])
        activity1 = Activities.objects.create(
            activity_name= activity['activity_name'],
            activity_description=activity['activity_description'],
            activity_address=activity['activity_address'],
            activity_start_time=activity['activity_starttime'],
            activity_end_time=activity['activity_endtime'],
            activity_credit=activity['activity_credit'],
            activity_max_size=activity['activity_max_size'],
            activity_type_id= activity['activity_type'],
            charger_id= activity['charger'],
            creater_id=admin1_id
        )
        if request.data['img'] != 'undefined':
            activity1.activity_img = request.data['img']
            activity1.save()
        ret={'code':'1001','msg':'添加成功'}
        return Response(json.dumps(ret))


class UpdateActivity(APIView):
    def post(self,request,*args,**kwargs):
        activity = json.loads(request.data['activity'])
        activity1 = Activities.objects.filter(activity_id=activity['activity_id']).first()
        activity1.activity_name= activity['activity_name']
        activity1.activity_description=activity['activity_description']
        activity1.charger_id = activity['charger_id']
        activity1.activity_address=activity['activity_address']
        activity1.activity_start_time=activity['activity_start_time']
        activity1.activity_end_time=activity['activity_end_time']
        activity1.activity_credit=activity['activity_credit']
        activity1.activity_max_size=activity['activity_max_size']
        activity1.activity_type_id= activity['activity_type']['type_id']
        if request.data['img'] != 'undefined':
            activity1.activity_img = request.data['img']
        activity1.save()
        activity1 = Activities.objects.filter(activity_id=activity['activity_id']).first()
        now1 = datetime.datetime.now()
        now1 = now1.replace(tzinfo=pytz.timezone('Asia/Shanghai'))
        if activity1.activity_end_time < now1:
            activity1.activity_status = 3
            activity1.save()
        else:
            if activity1.activity_start_time < now1:
                activity1.activity_status = 2
            else:
                activity1.activity_status = 1
        activity1.save()
        ret={'code':'1001','msg':'修改成功'}
        return Response(json.dumps(ret))


class DelActivity(APIView):
    def post(self,request,*args,**kwargs):
        id = request.data['activity_id']
        ac1 = Activities.objects.get(pk=int(id))
        ac1.activity_status = 0
        ac1.save()
        ret = {'code':'1001','msg': '删除成功'}
        return Response(json.dumps(ret))


class SchoolList(APIView):
    def get(self,request,*args,**kwargs):
        schools = Schools.objects.all()
        ret = SchoolSerializer(instance=schools,many=True)
        return  Response(ret.data)


class ChargerList(APIView):
    def get(self, request, *args, **kwargs):
        token = request._request.GET.get('token')
        school_id = Admins.objects.filter(admintoken__token=token).first().school.school_id
        print(school_id)
        if school_id == '0':
            ch = Chargers.objects.filter(charger_status=1,school_id=school_id)

        else:
            ch = Chargers.objects.filter(charger_status=1,school_id=int(school_id))
        # 创建分页对象
        pg = MyNumberPagination()
        # 获取分页的数据
        pg_types = pg.paginate_queryset(queryset=ch, request=request, view=self)
        # 序列化
        ret = ChargerSerializer(instance=pg_types, many=True)
        return pg.get_paginated_response(ret.data)


class AddCharger(APIView):
    def post(self,request,*args,**kwargs):
        charger = json.loads(request.data['charger'])
        token = request.data['token']
        school_id = AdminToken.objects.filter(token=token).first().user.school_id
        Chargers.objects.create(
            charger_name=charger['charger_name'],
            charger_password=charger['charger_password'],
            school_id=school_id,
            charger_phone=charger['charger_phone']
        )
        ret ={'code':'1002','msg':'添加成功'}
        return Response(ret)


class UpdateCharger(APIView):
    def post(self,request,*args,**kwargs):
        charger = json.loads(request.data['charger'])
        charger1 = Chargers.objects.filter(charger_id=charger['charger_id']).first()
        charger1.charger_name=charger['charger_name']
        charger1.charger_password=charger['charger_password']
        charger1.school_id=charger['school']['school_id']
        charger1.charger_phone=charger['charger_phone']
        charger1.save()
        ret ={'code':'1002','msg':'修改成功'}
        return Response(ret)

class DelCharger(APIView):
    def get(self,request,*args,**kwargs):
        id = request._request.GET.get('charger_id')
        ac1 = Chargers.objects.get(pk=int(id))
        ac1.charger_status = 0
        ac1.save()
        ret = {'code':'1001','msg': '删除成功'}
        return Response(json.dumps(ret))


class AddNotice(APIView):
    def post(self,request,*args,**kwargs):
        notice = json.loads(request.data['notice'])
        admin1_id = AdminToken.objects.filter(token=request.data['token']).first().user_id
        Notice.objects.create(
            notice_title=notice['notice_title'],
            notice_content=notice['notice_content'],
            creater_id= admin1_id
        )
        ret = {'code': '1002', 'msg': '添加成功'}
        return Response(ret)


class AllNotices(APIView):
    def get(self, request, *args, **kwargs):
        notice = Notice.objects.filter(notice_status=1)
        # 创建分页对象
        pg = MyNumberPagination()
        # 获取分页的数据
        pg_types = pg.paginate_queryset(queryset=notice, request=request, view=self)
        # 序列化
        ret = NoticeSerializer(instance=pg_types, many=True)
        return pg.get_paginated_response(ret.data)


class UpdateNotice(APIView):
    def post(self,request,*args,**kwargs):
        notice = json.loads(request.data['notice'])
        notice1 = Notice.objects.filter(notice_id=notice['notice_id']).first()
        notice1.notice_title = notice_title=notice['notice_title']
        notice1.notice_content = notice['notice_content']
        notice1.save()
        ret = {'code': '1002', 'msg': '修改成功'}
        return Response(ret)


class DelNotice(APIView):
    def get(self,request,*args,**kwargs):
        id = request._request.GET.get('notice_id')
        notice1 = Notice.objects.get(pk=int(id))
        notice1.notice_status = 0
        notice1.save()
        ret = {'code':'1001','msg': '删除成功'}
        return Response(json.dumps(ret))


class ClassInf(APIView):
    def get(self,request,*args,**kwargs):
        token = request._request.GET.get('token')
        school_id = Admins.objects.filter(admintoken__token=token).first().school.school_id
        students = Students.objects.filter(classes__major__department__school_id = school_id,student_status=1)
        print(school_id, type(school_id))
        pg = MyNumberPagination()
        pg_students = pg.paginate_queryset(queryset=students,request=request, view=self)
        departments = Departments.objects.filter(school_id=school_id)
        majors = Majors.objects.filter(department_id=departments[0].department_id)
        classes = Classes.objects.filter(major_id=majors[0].major_id)
        ret={}
        ret['departments'] = DepartmentSerializer(instance=departments,many=True).data
        ret['majors'] = MajorSerializer(instance=majors,many=True).data
        ret['classes'] = ClassSerializer(instance=classes,many=True).data
        ser_students = StudentSerializer(instance=pg_students,many=True).data
        ret['students'] = pg.get_paginated_response(ser_students).data
        return Response(ret)


class SchoolChange(APIView):
    def get(self,request,*args,**kwargs):
        school = request._request.GET.get('school')
        ret = {}
        departments = Departments.objects.filter(school_id=int(school))
        ret['departments'] = DepartmentSerializer(instance=departments, many=True).data
        print(school,type(school))
        print(departments)
        if school == '0':
            students = Students.objects.filter(student_status=1,)
        else:
            majors = Majors.objects.filter(department_id=departments[0].department_id)
            classes = Classes.objects.filter(major_id=majors[0].major_id)
            ret['majors'] = MajorSerializer(instance=majors, many=True).data
            ret['classes'] = ClassSerializer(instance=classes, many=True).data
            students = Students.objects.filter(student_status=1,classes__major__department__school_id = int(school))
        pg = MyNumberPagination()
        pg_students = pg.paginate_queryset(queryset=students, request=request, view=self)
        ser_students = StudentSerializer(instance=pg_students, many=True).data
        ret['students'] = pg.get_paginated_response(ser_students).data
        return Response(ret)


class DepartmentChange(APIView):
    def get(self,request,*args,**kwargs):
        department = request._request.GET.get('department')
        token = request._request.GET.get('token')
        ret = {}
        majors = Majors.objects.filter(department_id=int(department))
        ret['majors'] = MajorSerializer(instance=majors, many=True).data
        school_id = Admins.objects.filter(admintoken__token=token).first().school.school_id
        if department == '0':
            students = Students.objects.filter(student_status=1,classes__major__department__school_id = school_id)
        else:
            classes = Classes.objects.filter(major_id=majors[0].major_id)
            ret['classes'] = ClassSerializer(instance=classes, many=True).data
            students = Students.objects.filter(student_status=1,classes__major__department_id=int(department))
        pg = MyNumberPagination()
        pg_students = pg.paginate_queryset(queryset=students, request=request, view=self)
        ser_students = StudentSerializer(instance=pg_students, many=True).data
        ret['students'] = pg.get_paginated_response(ser_students).data
        return Response(ret)


class MajorChange(APIView):
    def get(self,request,*args,**kwargs):
        major = request._request.GET.get('major')
        department = request._request.GET.get('department')
        ret = {}
        classes = Classes.objects.filter(major_id=int(major))
        if major =='0':
            students = Students.objects.filter(student_status=1,classes__major__department_id=int(department))
        else:
            ret['classes'] = ClassSerializer(instance=classes, many=True).data
            students = Students.objects.filter(student_status=1,classes__major_id=int(major))
        pg = MyNumberPagination()
        pg_students = pg.paginate_queryset(queryset=students, request=request, view=self)
        ser_students = StudentSerializer(instance=pg_students, many=True).data
        ret['students'] = pg.get_paginated_response(ser_students).data
        return Response(ret)


class ClassChange(APIView):
    def get(self,request,*args,**kwargs):
        major = request._request.GET.get('major')
        classs = request._request.GET.get('classs')
        ret = {}
        if classs =='0':
            students = Students.objects.filter(student_status=1,classes__major_id=int(major))
        else:
            students = Students.objects.filter(student_status=1,classes_id=int(classs))
        pg = MyNumberPagination()
        pg_students = pg.paginate_queryset(queryset=students, request=request, view=self)
        ser_students = StudentSerializer(instance=pg_students, many=True).data
        ret['students'] = pg.get_paginated_response(ser_students).data
        return Response(ret)


class AddStudent(APIView):
    def post(self,request,*args,**kwargs):
        student = json.loads(request.data['student'])
        Students.objects.create(
            student_name=student['student_name'],
            student_no=student['student_no'],
            student_password=student['student_password'],
            student_phone=student['student_phone'],
            classes_id= int(student['classs'])
        )
        ret = {'code': '1002', 'msg': '添加成功'}
        return Response(ret)

class StudentClass(APIView):
    def get(self,request,*args,**kwargs):
        token = request._request.GET.get('token')
        class_id = request._request.GET.get('class_id')
        major_id = Classes.objects.filter(class_id=class_id).first().major_id
        classes = Classes.objects.filter(major_id=major_id)
        department_id = Majors.objects.filter(major_id=major_id).first().department_id
        majors = Majors.objects.filter(department_id=department_id)
        ret={}
        ret['classes'] = ClassSerializer(instance=classes,many=True).data
        ret['majors'] = MajorSerializer(instance=majors,many=True).data
        return Response(ret)

class ChangeStudent(APIView):
    def get(self,request,*args,**kwargs):
        token = request._request.GET.get('token')
        school_id = Admins.objects.filter(admintoken__token=token).first().school.school_id
        department = request._request.GET.get('department')
        major = request._request.GET.get('major')
        classs = request._request.GET.get('classs')
        if department == '0':
            students = Students.objects.filter(student_status=1,classes__major__department__school_id = school_id)
        else:
            if major == '0':
                students = Students.objects.filter(student_status=1,classes__major__department_id=int(department))
            else:
                if classs == '0':
                    students = Students.objects.filter(student_status=1,classes__major_id=int(major))
                else:
                    students = Students.objects.filter(student_status=1,classes_id=int(classs))
        pg = MyNumberPagination()
        pg_student = pg.paginate_queryset(queryset=students,request=request,view=self)
        ser_student = StudentSerializer(instance=pg_student,many=True)
        return pg.get_paginated_response(ser_student.data)


class UpdateStudent(APIView):
    def post(self,request,*args,**kwargs):
        student =json.loads(request.data['student'])
        student_id = student['student_id']
        classs= student.get('classs',None)
        student1 = Students.objects.filter(student_id=student_id).first()
        student1.student_name = student['student_name']
        student1.student_no = student['student_no']
        student1.student_phone = student['student_phone']
        student1.student_password = student['student_password']
        if classs != None:
            student1.classes_id = student['classs']
        student1.save()
        ret = {'code':'1001','msg':'修改成功'}
        return Response(json.dumps(ret))


class DeleteStudent(APIView):
    def get(self,request,*args,**kwargs):
        id = request._request.GET.get('student_id')
        ac1 = Students.objects.get(pk=int(id))
        ac1.student_status = 0
        ac1.save()
        ret = {'code': '1001', 'msg': '删除成功'}
        return Response(json.dumps(ret))


class StuedntActivityId(APIView):
    def get(self, request, *args, **kwargs):
        token = request._request.GET.get('token')
        student_id = Students.objects.filter(studenttoken__token=token).first().student_id
        student_activities = StuedntActivity.objects.filter(student_id=student_id).values('activity_id')
        s = list(student_activities)
        sc = [i['activity_id'] for i in s]
        return Response(sc)


class AllStuedntActivity(APIView):
    def get(self, request, *args, **kwargs):
        token = request._request.GET.get('token')
        type_id = request._request.GET.get('type_id')
        activity_status = request._request.GET.get('activity_status')
        print(int(activity_status))
        student_id = Students.objects.filter(studenttoken__token=token).first().student_id
        if type_id == '0':  # 判断是否是全部类型
            if activity_status == '4':  # 判断是否是全部状态
                ac = Activities.objects.filter(stuedntactivity__student_id=student_id,
                                               activity_status__in=[1, 2, 3])
            else:
                ac = Activities.objects.filter(stuedntactivity__student_id=student_id,
                                               activity_status=activity_status)
        else:
            if activity_status == '4':  # 判断是否是全部状态
                ac = Activities.objects.filter(activity_type_id=int(type_id),
                                               activity_status__in=[1, 2, 3],
                                               stuedntactivity__student_id=student_id )
            else:
                ac = Activities.objects.filter(activity_type_id=int(type_id),
                                               activity_status=int(activity_status),
                                               stuedntactivity__student_id=student_id)
        pg = MyNumberPagination()
        # 获取分页的数据
        pg_types = pg.paginate_queryset(queryset=ac, request=request, view=self)
        # 序列化
        ret = ActiviySerializer(instance=pg_types, many=True)
        return pg.get_paginated_response(ret.data)


class RegActivity(APIView):
    def post(self, request, *args, **kwargs):
        token = request.data['token']
        student_id = Students.objects.filter(studenttoken__token=token).first().student_id
        activity_id = request.data['activity_id']
        activity1 = Activities.objects.filter(activity_id=activity_id).first()
        activity1.activity_attend_size = activity1.activity_attend_size + 1
        activity1.save()
        StuedntActivity.objects.create(
            student_id = student_id,
            activity_id = activity_id
        )
        ret = {'code':'1001','msg':'报名成功'}
        return Response(ret)


class CancelActivity(APIView):
    def post(self, request, *args, **kwargs):
        token = request.data['token']
        student_id = Students.objects.filter(studenttoken__token=token).first().student_id
        activity_id = request.data['activity_id']
        activity1 = Activities.objects.filter(activity_id=activity_id).first()
        activity1.activity_attend_size = activity1.activity_attend_size - 1
        activity1.save()
        print(activity_id,type(activity_id))
        StuedntActivity.objects.filter(
            student_id = student_id,
            activity_id = int(activity_id)
        ).delete()
        ret = {'code':'1001','msg':'取消报名成功'}
        return Response(ret)


class StuedntInfo(APIView):
    def get(self,request,*args,**kwargs):
        token = request._request.GET.get('token')
        student= Students.objects.filter(studenttoken__token=token).first()
        ret = StudentSerializer(instance=student,many=False)
        return Response(ret.data)


class ActivityDetail(APIView):
    def get(self, request, *args, **kwargs):
        activity_id = request._request.GET.get('activity_id')
        activity1 = Activities.objects.filter(activity_id=activity_id).first()
        students = StuedntActivity.objects.filter(activity_id=activity_id)
        pg = MyNumberPagination()
        pg_students=pg.paginate_queryset(queryset=students,request=request,view=self)
        ser_students = StudentActivitySerializer(instance=pg_students, many=True).data
        ret = {}
        ret['students'] = pg.get_paginated_response(ser_students).data
        ret['activity'] = ActiviySerializer(instance=activity1, many=False).data
        return Response(ret)


class ChargerInfo(APIView):
    def get(self,request,*args,**kwargs):
        token = request._request.GET.get('token')
        charger= Chargers.objects.filter(chargetoken__token=token).first()
        ret = ChargerSerializer(instance=charger,many=False)
        return Response(ret.data)


class CreditInfo(APIView):
    def get(self,request,*args,**kwargs):
        token = request._request.GET.get('token')
        student_id = Students.objects.filter(studenttoken__token=token).first().student_id
        activity_types = ActivityTypes.objects.all()
        ret={}
        sum = 0
        for i in activity_types:
            activities = StuedntActivity.objects.filter(activity__activity_type__type_id=i.type_id,                                          student__student_id=student_id)
            score = 0
            for j in activities:
                score = score + j.credit
            sum += score
            ret[i.type_name] = score
            ret['总计'] = sum
        return Response(ret)


class DownloadCredit(APIView):
    def get(self, request, *args, **kwargs):
        token = request._request.GET.get('token')
        student = Students.objects.filter(studenttoken__token=token).first()
        student_activity = StuedntActivity.objects.filter(student_id=student.student_id)
        print(student_activity)
        fold_name = 'static/media/studentcredit'
        file_name = '学分详情-'+ student.student_name + '.xls'
        # file_name = 'credit.xls'
        excelPath = fold_name + '/' + file_name  # excel文件路径
        workbook = xlwt.Workbook(encoding='UTF-8')  # 创建工作簿对象
        sheet = workbook.add_sheet('学分详情')  # 创建工作表
        headers = ['活动名称','活动类型','活动时间','签到状态','签退状态','活动学分','获得学分']
        headstyle = xlwt.easyxf('font:color-index black,bold on')
        for colindex in range(7):
            sheet.write(0,colindex,headers[colindex],headstyle)  # 写入表头
        # workbook.save()  # 保存
        rowIndex = 1
        sum_credit = 0
        for i in range(len(student_activity)):
            # oldWorkbook = xlrd.open_workbook(excelPath,formatting_info=True)  # 打开文件并保留原有格式
            # newWorkbook = copy(oldWorkbook)  # 拷贝
            # sheet = newWorkbook.get_sheet(0)
            sheet.write(rowIndex,0,student_activity[i].activity.activity_name)  # 活动名称
            sheet.write(rowIndex,1,student_activity[i].activity.activity_type.type_name)  # 活动类型名称
            start_time = student_activity[i].activity.activity_start_time.strftime('%Y-%m-%d %H:%M:%S')  # 活动开始时间
            end_time = student_activity[i].activity.activity_end_time.strftime('%Y-%m-%d %H:%M:%S')  # 活动结束时间
            ac_time = start_time +' 至 ' + end_time
            sheet.write(rowIndex,2,ac_time)
            if student_activity[i].signin_status == 1:
                signin_status = '已签'
            else:
                signin_status = '未签'
            sheet.write(rowIndex,3, signin_status)  # 签到状态
            if student_activity[i].signout_status == 1:
                signout_status = '已签'
            else:
                signout_status = '未签'
            sheet.write(rowIndex,4, signout_status)   # 签退状态
            sheet.write(rowIndex,5,student_activity[i].activity.activity_credit)  # 活动学分
            sheet.write(rowIndex,6,student_activity[i].credit)  # 获得学分
            rowIndex += 1
            sum_credit += student_activity[i].credit
        sheet.col(0).width = 256 * 16  # 设置第一列为16个字符宽度
        sheet.col(1).width = 256 * 16
        sheet.col(2).width = 256 * 40
        sheet.write(rowIndex,0,'总计',headstyle)
        sheet.write(rowIndex,6,sum_credit,headstyle)
        workbook.save(excelPath)  # 保存
        file1 = open(excelPath,'rb')
        print(excelPath)
        print(file_name)
        ret = HttpResponse(file1)
        ret["Content-Type"] = "application/octet-stream"  # 注意格式
        ret["Content-Disposition"] = 'attachment;filename={}'.format(file_name.encode('utf-8').decode('ISO-8859-1'))
        return ret


class SignIn(APIView):
    def get(self, request, *args, **kwargs):
        student_activity_id = request._request.GET.get('student_activity_id')
        print(student_activity_id)
        student_activity = StuedntActivity.objects.filter(id=int(student_activity_id)).first()
        student_activity.signin_status = 1
        student_activity.save()
        ret={'code':'1001','msg':'签到成功'}
        return Response(ret)


class SignOut(APIView):
    def get(self, request, *args, **kwargs):
        student_activity_id = request._request.GET.get('student_activity_id')
        print(student_activity_id)
        student_activity = StuedntActivity.objects.filter(id=int(student_activity_id)).first()
        student_activity.signout_status = 1
        student_activity.save()
        ret={'code':'1001','msg':'签退成功'}
        return Response(ret)


class GiveCredit(APIView):
    def get(self, request, *args, **kwargs):
        student_activity_id = request._request.GET.get('student_activity_id')
        credit = request._request.GET.get('credit')
        print(student_activity_id)
        student_activity = StuedntActivity.objects.filter(id=int(student_activity_id)).first()
        student_activity.credit = float(credit)
        student_activity.save()
        ret={'code':'1001','msg':'打分成功'}
        return Response(ret)