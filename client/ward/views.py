from django.shortcuts import render,reverse
from .models import *
from django.http import JsonResponse
# Create your views here.


def addward(request):
    """
     添加病房
    :param request:
    :return:
    """
    if request.method == 'GET':
        roomtypes = RoomType.objects.all()
        return render(request,'add-room.html',locals())
    if request.method == 'POST':
        room_name = request.POST.get('room_name')  # 病房名
        type_id = request.POST.get('room_type')  # 病房类型编号
        room_capicity = request.POST.get('room_capacity')  #最大容量
        room_type = RoomType.objects.get(pk=type_id)  # 病房类型
        types = RoomType.objects.all()  # 所有病房类型
        print(room_capicity)
        if room_capicity == '' or room_name == '':  # 验证表单信息是否完整
            return render(request,'add-room.html',{'room_name':room_name,'room_captcity':room_capicity,'roomtypes':types,'msg':'信息填写有误，请重新输入！'})
        room = Room.objects.create(room_name=room_name,room_type=room_type,room_capacity=room_capicity)
        for i in range(int(room_capicity)):
            RoomBed.objects.create(room=room,bed_name=i+1)  # 创建病床
        rooms = Room.objects.all()
        livein = []
        for room in rooms:
            num = room.roombed_set.filter(bed_status=1).count()
            livein.append(num)
        print(livein)
        data = zip(rooms, livein)
        return render(request, 'rooms.html', {'data': data,'msg':'病房添加成功!'})


def inward(request,id):
    """
    病人住院
    :param request:
    :param id: 病人编号
    :return:
    """
    if request.method == 'GET':
        patient = Patient.objects.get(pk=id)
        roomtypes = RoomType.objects.all()  # 病房类型
        rooms = Room.objects.filter(
            room_type=roomtypes.first(),
        )
        rooms = list(rooms)  # 初始病房列表
        for room in rooms:
            beds = RoomBed.objects.filter(room=room,bed_status=1)
            if len(list(beds)) == room.room_capacity:  # 判断病房是否已经住满
                rooms.remove(room)
        beds = RoomBed.objects.filter(room=rooms[0],bed_status=0)  # 初始病床
        print(patient.p_id)
        return render(request,'edit-room.html',locals())
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')  # 病人编号
        room_type_id = request.POST.get('room_type_id')  # 病床类型
        room_id = request.POST.get('room_id')  # 病房编号
        bed_id = request.POST.get('bed_id')  # 病床号
        patient = Patient.objects.get(pk=patient_id)  # 病人编号
        room = Room.objects.get(pk=room_id)  # 病房
        bed = RoomBed.objects.get(pk=bed_id)
        treat = patient.treat_set.filter(treat_status=1).first()
        print(treat)
        roompatient = RoomPatien.objects.create(
            treat= treat,
            patient=patient,
            bed=bed,
        )
        bed = RoomBed.objects.get(pk=bed_id)
        bed.bed_status = 1
        bed.save()
        treats = Treat.objects.all()
        return render(request, 'appointments.html', {"treats": treats,'msg':'病人入住成功！'})


def roomtypeajax(request):
    """
    选择病房类型联动下拉框
    :param request:
    :return:
    """
    type_id = request.GET.get('type_id')  # 病房类型id
    roomtype = RoomType.objects.get(pk=type_id)  # 选中的病房类型
    rooms = Room.objects.filter(room_type=roomtype)  # 所有病房
    room1 = Room.objects.filter(room_type=roomtype).values('room_id','room_name')
    rooms = list(rooms)
    for room in list(rooms):
        beds = RoomBed.objects.filter(room=room, bed_status=1)
        if len(list(beds)) == room.room_capacity:  # 判断病房是否已经住满
            rooms.remove(room)      # 删除病房床位数量为0的
    beds = RoomBed.objects.filter(room=rooms[0], bed_status=0).values('bed_id','bed_name')  #所有床位
    data = [list(room1),list(beds)]
    return JsonResponse(data, safe=False)


def roomajax(request):
    """
    选择病房联动下拉框
    :param request:
    :return:
    """
    room_id = request.GET.get('room_id')  # 病房id
    room = Room.objects.get(pk=room_id)
    beds = RoomBed.objects.filter(room=room, bed_status=0).values('bed_id','bed_name')  # 所有床位
    data = list(beds)
    return JsonResponse(data, safe=False)


def outward(request,id):
    """
    病人出院
    :param request: 出诊信息编号
    :param id:
    :return:
    """
    patient = Patient.objects.get(pk=id)  # 病人编号
    patient.p_status = PatientStatus.objects.get(pk=1)  # 将病人状态设置为未挂号状态
    patient.save()
    treat = patient.treat_set.filter(treat_status=1).first()  # 出诊信息
    treat.treat_status = 0  # 将治疗状态设置为已治愈
    treat.save()
    register = treat.register
    register.reg_status = 0  # 将病人挂号状态设置为已完成状态
    register.save()
    try:
        roompatient = treat.roompatien_set.first()
        roompatient.status = 0  # 将病人住院状态置空
        roompatient.save()
        bed = roompatient.bed
        bed.bed_status = 0  # 将病人住的病床置空
        bed.save()
    except:
        pass
    rooms = Room.objects.all()
    livein = []
    for room in rooms:
        num = room.roombed_set.filter(bed_status=1).count()
        livein.append(num)
    print(livein)
    data = zip(rooms, livein)
    return render(request, 'rooms.html', {'data': data,'msg':'病人已出院！'})


def showward(request):
    """
    病房列表
    :param request:
    :return:
    """
    rooms = Room.objects.all()
    livein = []
    for room in rooms:
        num = room.roombed_set.filter(bed_status=1).count()
        livein.append(num)
    print(livein)
    data = zip(rooms,livein)  # 将两个列表压缩成字典，便于同时遍历
    treats = Treat.objects.all()
    return render(request,'appointments.html',{'data':data,"treats": treats})


def aboutward(request,id):
    """
    病房详情
    :param request: 病房id
    :param id:
    :return:
    """
    room = Room.objects.get(pk=id)
    beds = room.roombed_set.all()
    patients = []
    for bed in beds:
        rpatient = bed.roompatien_set.filter(status=1).first()
        if rpatient:
            patients.append(rpatient.patient.p_name)
        else:
            patients.append(0)
    data = zip(beds,patients)  # 将两个列表压缩成字典，便于同时遍历
    return render(request,'about-room.html',locals())