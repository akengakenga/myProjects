from django.db import models
from django.utils import timezone
# Create your models here.
#用户信息
class User(models.Model):
    user_id = models.AutoField(verbose_name="用户ID",primary_key=True)
    user_name = models.CharField(max_length=32,verbose_name="用户名",unique=True)
    user_password = models.CharField(max_length=32,verbose_name="密码")
    userDetail = models.OneToOneField(to="UserDetail",on_delete=models.CASCADE)
# 用户详情
class UserDetail(models.Model):
    uinf_id = models.AutoField(verbose_name="用户ID",primary_key=True)
    uinf_email = models.EmailField(verbose_name="邮箱")
    uinf_sex = models.CharField(max_length=4,verbose_name="性别",default="保密")
    uinf_mobile = models.CharField(max_length=11,verbose_name="手机号码")
    uinf_url = models.CharField(max_length=100,verbose_name="个人博客地址")
    uinf_sign = models.CharField(max_length=200)
    uinf_avatar = models.ImageField(upload_to='avatar/%Y/%m', default='blog/avatar/default.png', max_length=200, blank=True, null=True, verbose_name='用户头像')

class Article(models.Model):
    art_id = models.AutoField(verbose_name="文章ID",primary_key=True)
    art_title = models.CharField(max_length=30,verbose_name="标题",)
    art_content = models.TextField(verbose_name="正文")
    art_time = models.DateTimeField(verbose_name="修改时间",default=timezone.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
class Comment(models.Model):
    comm_id = models.AutoField(verbose_name="评论ID",primary_key=True)
    comm_content = models.CharField(max_length=100,verbose_name="评论内容")
    comm_time = models.DateTimeField(verbose_name="修改时间", default=timezone.now)
    art_id = models.ForeignKey(Article,on_delete=models.CASCADE)