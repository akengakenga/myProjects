from django.db import models
from president.models import *
from doctor.models import *
from patient.models import *
# Create your models here.


class Treat(models.Model):
    treat_id = models.AutoField(verbose_name='编号',primary_key=True)
    patient = models.ForeignKey(Patient,verbose_name='病人',on_delete=models.CASCADE,db_constraint=models.CASCADE)
    register = models.ForeignKey(Register,verbose_name='挂号单',on_delete=models.CASCADE,db_constraint=models.CASCADE)
    doctor = models.ForeignKey(Doctor,verbose_name='主治医生',on_delete=models.CASCADE,db_constraint=models.CASCADE)
    treat_time = models.DateTimeField(verbose_name='治疗日期',auto_now=True)
    treat_active = models.IntegerField(verbose_name='治疗激活状态',default=1)   # 1表示激活  0表示未激活
    treat_problem = models.CharField(verbose_name='病因',max_length=500)
    treat_status = models.IntegerField(verbose_name='治疗状态',default=1)  # 1表示治疗中  0表示已治愈
    objects = models.Manager()

    class Meta():
        verbose_name = '出诊信息'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s

    def __str__(self):
        return str(self.treat_id)
