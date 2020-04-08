from django.db import models

# Create your models here.


class UserType(models.Model):
    type_id = models.AutoField(verbose_name='编号',primary_key=True)
    type_name = models.CharField(verbose_name='类型',max_length=50)
    objects = models.Manager()

    class Meta():
        verbose_name = '用户类型'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s

    def __str__(self):
        return self.type_name


class President(models.Model):
    pre_id = models.AutoField(verbose_name='编号',primary_key=True)
    pre_name = models.CharField(verbose_name='姓名',max_length=10)
    pre_password = models.CharField(verbose_name='密码',max_length=20)
    user_type = models.ForeignKey(UserType,verbose_name='用户类型',on_delete=models.CASCADE,db_constraint=models.CASCADE,default=1)
    objects = models.Manager()

    class Meta():
        verbose_name = '院长'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s

    def __str__(self):
        return self.pre_name

