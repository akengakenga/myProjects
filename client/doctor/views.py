from django.shortcuts import render,redirect,reverse
from .models import *
from president.models import *
# Create your views here.


def showdoctor(request):
    """
    医生列表
    :param request:
    :return:
    """
    doctors = Doctor.objects.all()
    return render(request,'doctors.html',{'doctors':doctors})


def adddoctor(request):
    """
    添加医生
    :param request:
    :return:
    """
    if request.method == 'GET':
        doctortypes = DoctorType.objects.all()
        return render(request,'add-doctor.html',{"doctortypes":doctortypes})
    if request.method == 'POST':
        doc_image = request.FILES.get('doc_image')
        doc_name = request.POST.get('doc_name')
        doc_birth = request.POST.get('doc_birth')
        doc_password = request.POST.get('doc_password')
        doc_experience = request.POST.get('doc_experience')
        doc_phone = request.POST.get('doc_phone')
        doc_email = request.POST.get('doc_email')
        doc_gender = request.POST.get('doc_gender')
        doc_type = request.POST.get('doc_type')
        doc_address = request.POST.get('doc_address')
        try:
            Doctor.objects.create(
                doc_image = doc_image,
                doc_name = doc_name,
                doc_birth = doc_birth,
                doc_password = doc_password,
                doc_experience = doc_experience,
                doc_phone = doc_phone,
                doc_email = doc_email,
                doc_gender = doc_gender,
                doc_type = DoctorType.objects.get(pk=doc_type),
                doc_address = doc_address
            )
        except:
            msg = '信息填写有误，请检查并重新填写！'
            doctortypes = DoctorType.objects.all()
            return render(request,'add-doctor.html',locals())
        else:
            doctors = Doctor.objects.all()
            return render(request, 'doctors.html', {'doctors': doctors,'msg':'医生添加成功！'})


def updatedoctor(request,id):
    """
    修改医生信息
    :param request:
    :param id: 医生id
    :return:
    """
    if request.method == 'GET':
        doctor = Doctor.objects.get(pk=id)
        doctortypes = DoctorType.objects.all()
        return render(request,'edit-doctor.html',{'doctor':doctor,'doctortypes':doctortypes})
    if request.method == 'POST':
        doc_image = request.FILES.get('doc_image')
        doc_name = request.POST.get('doc_name')
        doc_birth = request.POST.get('doc_birth')
        doc_password = request.POST.get('doc_password')
        doc_experience = request.POST.get('doc_experience')
        doc_phone = request.POST.get('doc_phone')
        doc_email = request.POST.get('doc_email')
        doc_gender = request.POST.get('doc_gender')
        doc_type = request.POST.get('doc_type')
        doc_address = request.POST.get('doc_address')
        doctor = Doctor.objects.get(pk=id)
        try:
            if doc_image != None:  # 判断是否添加头像
                doctor.doc_image = doc_image
            doctor.doc_name=doc_name
            doctor.doc_birth=doc_birth
            doctor.doc_password=doc_password
            doctor.doc_experience=doc_experience
            doctor.doc_phone=doc_phone
            doctor.doc_email=doc_email
            doctor.doc_gender=doc_gender
            doctor.doc_type=DoctorType.objects.get(pk=doc_type)
            doctor.doc_address=doc_address
            doctor.save()
        except:
            msg = '信息填写有误，请检查并重新填写！'
            doctortypes = DoctorType.objects.all()
            return render(request, 'edit-doctor.html', locals())
        else:
            doctors = Doctor.objects.all()
            return render(request, 'doctors.html', {'doctors': doctors, 'msg': '医生修改成功！'})


def deletedoctor(request,ids):
    """
    删除医生信息
    :param request:
    :param ids: 医生id字符串
    :return:
    """
    ids = ids.split('_')
    try:
        for id in ids:   # 将字符串拆分成医生id
            doctor = Doctor.objects.get(pk=id)
            doctor.doc_active = 0   # 判断医生是否激活状态
            doctor.save()
    except:
        pass
    else:
        doctors = Doctor.objects.all()
        return render(request, 'doctors.html', {'doctors': doctors, 'msg': '医生删除成功！'})


def doctordetail(request,id):
    """
    医生详情
    :param request:
    :param id: 医生id
    :return:
    """
    doctor = Doctor.objects.get(pk=id)
    return render(request,'about-doctor.html',{'doctor':doctor})
