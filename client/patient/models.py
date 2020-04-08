from django.db import models
from president.models import *
from doctor.models import *
# Create your models here.
class PatientStatus(models.Model):
    status_id = models.AutoField(verbose_name='编号',primary_key=True)
    status_name = models.CharField(verbose_name='状态',max_length=50)

    class Meta():
        verbose_name = '病人状态'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s

    def __str__(self):
        return self.status_name

class Patient(models.Model):
    p_id = models.AutoField(verbose_name='编号',primary_key=True)
    p_name = models.CharField(verbose_name='姓名',max_length=10)
    p_password = models.CharField(verbose_name='密码',max_length=20)
    p_birth = models.DateField(verbose_name='生日')
    p_gender = models.IntegerField(verbose_name='性别')
    p_email = models.EmailField(verbose_name='邮箱')
    p_address = models.CharField(verbose_name='地址',max_length=100)
    p_phone = models.CharField(verbose_name='手机',max_length=13)
    p_status = models.ForeignKey(PatientStatus,verbose_name='状态',on_delete=models.CASCADE,db_constraint=models.CASCADE,default=1)
    p_active = models.IntegerField(verbose_name='病人激活状态' ,default=1)  # 1表示激活  0表未激活
    user_type = models.ForeignKey(UserType,verbose_name='类型',on_delete=models.CASCADE,db_constraint=models.CASCADE,default=3)

    class Meta():
        verbose_name = '病人'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s

    def __str__(self):
        return self.p_name

class Register(models.Model):
    reg_id = models.AutoField(verbose_name='编号',primary_key=True)
    reg_patient = models.ForeignKey(Patient,verbose_name='病人编号',on_delete=models.CASCADE,db_constraint=models.CASCADE)
    reg_time = models.DateTimeField(verbose_name='挂号时间',auto_now=True)
    reg_type = models.ForeignKey(DoctorType,verbose_name='挂号类型',on_delete=models.CASCADE,db_constraint=models.CASCADE)
    reg_status = models.IntegerField(verbose_name='状态',default=1)  # 1表示进行中   0表示完成

    class Meta():
        verbose_name = '挂号表'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s

    def __str__(self):
        return str(self.reg_id)