from django.db import models
from logManager.models import *
# Create your models here.
status = (
        (1, '已注册'),
        (0, '未注册')
)


class ActivityTypes(models.Model):
    type_id = models.AutoField(verbose_name='编号',primary_key=True)
    type_name = models.CharField(verbose_name='活动类型',max_length=50)
    type_status = models.IntegerField(choices=status,verbose_name='状态',default=1)

    def __str__(self):
            return self.type_name

    class Meta():
        verbose_name = '活动类型'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s


class Activities(models.Model):
    status = (
        (0, '未激活'),
        (1, '未开始'),
        (2, '进行中'),
        (3, '已经结束'),
    )
    activity_id = models.AutoField(verbose_name='编号',primary_key=True)
    activity_name = models.CharField(verbose_name='活动名称',max_length=50)
    activity_description = models.CharField(verbose_name='活动简介',max_length=1000)
    activity_img = models.ImageField(upload_to='activity/%Y/%m',verbose_name='活动图片',default='activity/default.png')
    activity_address = models.CharField(verbose_name='活动地点',max_length=100, blank=True, null=True)
    activity_start_time = models.DateTimeField(verbose_name='活动开始时间')
    activity_end_time = models.DateTimeField(verbose_name='活动结束时间')
    activity_max_size = models.IntegerField(verbose_name='容纳人数')
    activity_attend_size = models.IntegerField(verbose_name='已报名人数',default=0)
    activity_credit = models.FloatField(verbose_name='活动学分')
    activity_type = models.ForeignKey(ActivityTypes,verbose_name='活动类型',on_delete=models.CASCADE,db_constraint=models.CASCADE)
    activity_status = models.IntegerField(choices=status,verbose_name='活动状态',default=1)
    creater = models.ForeignKey(Admins,verbose_name='活动创建人',on_delete=models.CASCADE,db_constraint=models.CASCADE)
    charger = models.ForeignKey(Chargers,verbose_name='活动负责人',on_delete=models.CASCADE,db_constraint=models.CASCADE)

    def __str__(self):
            return self.activity_name

    class Meta():
        verbose_name = '活动'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s


class Notice(models.Model):
    notice_id = models.AutoField(verbose_name='编号',primary_key=True)
    notice_title = models.CharField(verbose_name='公告标题',max_length=50)
    notice_content = models.CharField(verbose_name='公告内容',max_length=2000)
    notice_create_time = models.DateTimeField(verbose_name='公告创建时间',auto_now_add=True)
    notice_status = models.IntegerField(verbose_name='公告状态',choices=status,default=1)
    creater = models.ForeignKey(Admins,verbose_name='公告创建人',on_delete=models.CASCADE,db_constraint=models.CASCADE)
    def __str__(self):
            return self.notice_title

    class Meta():
        verbose_name = '公告'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s


class StuedntActivity(models.Model):
    status = (
        (0, '未签'),
        (1, '已签'),
    )
    id = models.AutoField(verbose_name='编号',primary_key=True)
    student = models.ForeignKey(Students,verbose_name='学生编号',on_delete=models.CASCADE,db_constraint=models.CASCADE)
    activity = models.ForeignKey(Activities,verbose_name='活动编号',on_delete=models.CASCADE,db_constraint=models.CASCADE)
    signin_status = models.IntegerField(verbose_name='签到状态',choices=status,default=0)
    signout_status = models.IntegerField(verbose_name='签退状态',choices=status,default=0)
    credit = models.FloatField(verbose_name='获得学分',default=0)
