from django.db import models
from patient.models import *
from treat.models import *
# Create your models here.
from datetime import datetime

class RoomType(models.Model):
    type_id = models.AutoField(verbose_name='病房类型编号',primary_key=True)
    type_name = models.CharField(verbose_name='病房类型',max_length=30)
    objects = models.Manager()

    class Meta():
        verbose_name = '病房类型'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s

    def __str__(self):
        return self.type_name


class Room(models.Model):
    room_id = models.AutoField(verbose_name='病房号',primary_key=True)
    room_name = models.CharField(verbose_name='病房名称',max_length=20)
    room_capacity = models.IntegerField(verbose_name='容纳人数')
    room_type = models.ForeignKey(RoomType,verbose_name='病房类型',on_delete=models.CASCADE,db_constraint=models.CASCADE)
    objects = models.Manager()

    class Meta():
        verbose_name = '病房'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s

    def __str__(self):
        return self.room_id


class RoomBed(models.Model):
    bed_id = models.AutoField(verbose_name='编号',primary_key=True)
    bed_name = models.CharField(verbose_name='床号',max_length=10)
    bed_status = models.IntegerField(verbose_name='状态',default=0) #1表示有人   0表示没人
    room = models.ForeignKey(Room,verbose_name='所属病房',on_delete=models.CASCADE,db_constraint=models.CASCADE)
    objects = models.Manager()

    class Meta():
        verbose_name = '病床'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s

    def __str__(self):
        return self.bed_id


class RoomPatien(models.Model):
    id = models.AutoField(verbose_name='编号',primary_key=True)
    patient = models.ForeignKey(Patient,verbose_name='病人',on_delete=models.CASCADE,db_constraint=models.CASCADE)
    treat = models.ForeignKey(Treat,verbose_name='出诊记录',on_delete=models.CASCADE,db_constraint=models.CASCADE)
    bed = models.ForeignKey(RoomBed,verbose_name='床号',on_delete=models.CASCADE,db_constraint=models.CASCADE)
    checkin_time = models.DateTimeField(verbose_name='入住时间',auto_now_add=True)
    checkout_time = models.DateTimeField(verbose_name='出院时间',null=True,blank=True,auto_now=True)
    status = models.IntegerField(verbose_name='状态',default=1)   # 1表示有人  0表示没人
    objects = models.Manager()

    class Meta():
        verbose_name = '入住表'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s

    def __str__(self):
        return self.room.room_name

