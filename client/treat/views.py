from django.shortcuts import render
from django.http import JsonResponse
from doctor.models import *
from patient.models import *
from .models import *
# Create your views here.


def addtreat(request):
    """
    添加出诊信息
    :param request:
    :return:
    """
    if request.method == 'GET':
        types = DoctorType.objects.all()   # 默认挂号类型
        type1 = types.first()
        doctors = Doctor.objects.filter(doc_type=type1)  # 默认挂号类型对应科室医生列表
        p_status = PatientStatus.objects.get(pk=2)
        patients = Patient.objects.filter(  # 默认挂号类型对应挂号病人
            p_status=p_status,  # 病人状态（已挂号）
            register__reg_status = 1,  # 挂号状态（进行中）
            register__reg_type = type1)  # 挂号类型
        return render(request,'add-appointment.html',{'types':types,'patients':patients,'doctors':doctors})
    else:
        doctor_id = request.POST.get('doctor_id')
        doctor = Doctor.objects.filter(doc_id=doctor_id).first()
        patient_id = request.POST.get('patient_id')
        patient = Patient.objects.filter(p_id=patient_id).first()
        problem = request.POST.get('problem')
        register = Register.objects.filter(reg_patient=patient,reg_status=1).first()
        if doctor==None or patient==None or problem =='':  # 判断表单信息是否填写完整
            types = DoctorType.objects.all()
            type1 = types.first()
            doctors = Doctor.objects.filter(doc_type=type1)
            p_status = PatientStatus.objects.get(pk=2)
            patients = Patient.objects.filter(
                p_status=p_status,
                register__reg_status=1,
                register__reg_type=type1)
            return render(request, 'add-appointment.html', {'types': types, 'patients': patients, 'doctors': doctors,'problem':problem,'msg':'信息填写有误，请重新填写！'})
        treat = Treat.objects.create(doctor=doctor,patient=patient,treat_problem=problem,register=register)  # 添加出诊记录
        patient.p_status = PatientStatus.objects.get(pk=3)  # 将病人状态设置为治疗中
        patient.save()
        treats = Treat.objects.all()
        return render(request, 'appointments.html', {"treats": treats,'msg':'出诊信息添加成功！'})


def addtreatdetail(request):
    """
    出诊类型-->病人，医生 下拉框二级联动 ajax
    :param request:
    :return:
    """
    type_id = request.GET.get('type_id')  # 获取选择的出诊类型
    type = DoctorType.objects.get(pk=type_id)
    p_status = PatientStatus.objects.get(pk=2)  # 获取状态为已挂号的病人
    patients = Patient.objects.filter(
        p_status=p_status,
        register__reg_status = 1,
        register__reg_type = type
    ).values('p_name','p_id')
    doctors = Doctor.objects.filter(doc_type=type).values('doc_name', 'doc_id')
    print(list(patients))
    print(list(doctors))
    data = [list(patients),list(doctors)]
    return JsonResponse(data,safe=False)


def showtreat(request):
    """
    出诊记录列表
    :param request:
    :return:
    """
    treats = Treat.objects.all()
    return render(request,'appointments.html',{"treats":treats})


def updatetreat(request,id):
    """
    修改出诊记录
    :param request:
    :param id: 出诊记录id
    :return:
    """
    if request.method == 'GET':
        treat = Treat.objects.get(pk=id)
        return render(request,'edit-appointment.html',{'treat':treat})
    else:
        treat_id = request.POST.get('treat_id')
        treat_problem = request.POST.get('problem')
        treat = Treat.objects.get(pk=treat_id)
        if treat_problem == '':
            return render(request,'edit-appointment.html',{'treat':treat,'msg':'病因必须填写！'})
        else:
            treat.treat_problem = treat_problem
            treat.save()
            treats = Treat.objects.all()
            return render(request,'appointments.html',{'msg':'出诊信息修改成功','treats':treats})


def deletetreat(request,ids):
    """
    删除出诊记录
    :param request:
    :param ids: 出诊记录id
    :return:
    """
    ids = ids.split('_')
    print(ids)
    try:
        for id in ids:
            treat = Treat.objects.get(pk=id)
            treat.treat_active = 0
            treat.save()
    except:
        pass
    else:
        treats = Treat.objects.all()
        return render(request, 'appointments.html', {'treats': treats, 'msg': '出诊信息删除成功！'})

