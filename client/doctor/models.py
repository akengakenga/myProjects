from django.db import models
from president.models import *

app_name = 'doctor'
# Create your models here.


class DoctorType(models.Model):
    type_id = models.AutoField(verbose_name='编号',primary_key=True)
    type_name = models.CharField(verbose_name='类型',max_length=10)
    objects = models.Manager()

    class Meta():
        verbose_name = '类型'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s

    def __str__(self):
        return self.type_name


class Doctor(models.Model):
    doc_id = models.AutoField(verbose_name='编号',primary_key=True)
    doc_name = models.CharField(verbose_name='姓名',max_length=10)
    doc_password = models.CharField(verbose_name='密码',max_length=20)
    doc_birth = models.DateField(verbose_name='生日')
    doc_gender = models.IntegerField(verbose_name='性别')
    doc_email = models.EmailField(verbose_name='邮箱')
    doc_experience = models.IntegerField(verbose_name='执业时间')
    doc_address = models.CharField(verbose_name='地址',max_length=100)
    doc_phone = models.CharField(verbose_name='手机',max_length=13)
    doc_type = models.ForeignKey(DoctorType,verbose_name='类型',on_delete=models.CASCADE,db_constraint=models.CASCADE)
    doc_image = models.ImageField(verbose_name='照片',upload_to='doctor-headers')
    doc_active = models.IntegerField(verbose_name='医生激活状态',default=1)  # 1表示激活  0表示未激活
    user_type = models.ForeignKey(UserType,verbose_name='类型',on_delete=models.CASCADE,db_constraint=models.CASCADE,default=2)
    objects = models.Manager()

    class Meta():
        verbose_name = '医生'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s

    def __str__(self):
        return self.doc_name

