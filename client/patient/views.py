from django.shortcuts import render
from .models import *
from doctor.models import *
from treat.models import *
# Create your views here.


def showpatient(request):
    """
    病人列表
    :param request:
    :return:
    """
    patients = Patient.objects.all()
    return render(request,'patients.html',{'patients':patients})


def addpatient(request):
    """添加病人"""
    if request.method == 'GET':
        return render(request,'add-patient.html')
    if request.method == 'POST':
        p_name = request.POST.get('p_name')
        p_birth = request.POST.get('p_birth')
        p_password = request.POST.get('p_password')
        p_phone = request.POST.get('p_phone')
        p_email = request.POST.get('p_email')
        p_gender = request.POST.get('p_gender')
        p_address = request.POST.get('p_address')
        if p_name == "" or p_password == "" or p_phone == "" or p_email == "" or p_address == "":  # 检查表单信息是否填写完整
            msg = '信息填写有误，请检查并重新填写'
            return render(request, 'add-patient.html', locals())
        try:
            Patient.objects.create(
                p_name = p_name,
                p_birth = p_birth,
                p_password = p_password,
                p_phone = p_phone,
                p_email = p_email,
                p_gender = p_gender,
                p_address = p_address
            )
        except:
            msg = '信息填写有误，请检查并重新填写！'
            return render(request,'edit-patient.html',locals())
        else:
            patients = Patient.objects.all()
            return render(request, 'patients.html', {'patients': patients,'msg':'病人添加成功！'})


def updatepatient(request,id):
    """
    修改病人信息
    :param request:
    :param id: 病人id
    :return:
    """
    if request.method == 'GET':
        patient = Patient.objects.get(pk=id)
        return render(request, 'edit-patient.html',{'patient':patient})
    if request.method == 'POST':
        p_name = request.POST.get('p_name')
        p_birth = request.POST.get('p_birth')
        p_password = request.POST.get('p_password')
        p_phone = request.POST.get('p_phone')
        p_email = request.POST.get('p_email')
        p_gender = request.POST.get('p_gender')
        p_address = request.POST.get('p_address')
        patient = Patient.objects.get(pk=id)
        if p_name == "" or p_password == "" or p_phone == "" or p_email == "" or p_address == "":
            msg = '信息填写有误，请检查并重新填写'
            return render(request, 'edit-patient.html', locals())
        try:
            patient.p_name=p_name
            patient.p_birth=p_birth
            patient.p_password=p_password
            patient.p_phone=p_phone
            patient.p_email=p_email
            patient.p_gender=p_gender
            patient.p_address=p_address
            patient.save()
        except:
            msg = '信息填写有误，请检查并重新填写！'
            return render(request, 'edit-patient.html', locals())
        else:
            patients = Patient.objects.all()
            return render(request, 'patients.html', {'patients': patients, 'msg': '病人修改成功！'})


def deletepatient(request,ids):
    """
    删除病人
    :param request:
    :param ids: 病人id
    :return:
    """
    ids = ids.split('_')
    try:
        for id in ids:  # 将字符串拆分成病人id  循环删除病人
            patient = Patient.objects.get(pk=id)
            patient.p_active = 0
            patient.save()
    except:
        pass
    else:
        patients = Patient.objects.all()
        return render(request, 'patients.html', {'patients': patients, 'msg': '病人删除成功！'})


def patientdetail(request,id):
    """
    病人详情
    :param request:
    :param id: 病人id
    :return:
    """
    patient = Patient.objects.get(pk=id)
    treats = Treat.objects.filter(patient=patient).all()
    return render(request, 'about-patient.html', {'patient': patient,'treats':treats})


def patientregister(request,id):
    """
    病人挂号
    :param request:
    :param id: 病人id
    :return:
    """
    if request.method == 'GET':
        types = DoctorType.objects.all()
        patient = Patient.objects.get(pk=id)
        return render(request,'patientregister.html',{'types':types,'patient':patient})
    else:
        patient_id = request.POST.get('p_id')  # 病人编号
        type_id = request.POST.get('type_id')  # 挂号类型
        patient = Patient.objects.get(pk=patient_id)
        patient_status = PatientStatus.objects.get(pk=2)
        patient.p_status = patient_status
        patient.save()
        doctor_type = DoctorType.objects.get(pk=type_id)
        register = Register.objects.create(
            reg_patient = patient,
            reg_type = doctor_type
        )
        patients = Patient.objects.all()
        return render(request,'patients.html',{'patients':patients,'msg':'挂号成功！'})

