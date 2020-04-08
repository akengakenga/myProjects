from django.db import models

# Create your models here.
status = (
        (1, '已注册'),
        (0, '未注册')
    )

types = (
        (1, '系统管理员'),
        (2, '活动负责人'),
        (3, '学生')
    )


class Schools(models.Model):
    school_id = models.AutoField(verbose_name='编号',primary_key=True)
    school_name = models.CharField(verbose_name='学校名称',max_length=50)
    school_status = models.IntegerField(verbose_name='学校状态',choices=status,default=1)

    def __str__(self):
        return self.school_name

    class Meta():
        verbose_name = '学校'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s


class Departments(models.Model):
    department_id = models.AutoField(verbose_name='编号',primary_key=True)
    department_name = models.CharField(verbose_name='学院名称',max_length=50)
    department_status = models.IntegerField(verbose_name='学院状态',choices=status,default=1)
    school = models.ForeignKey(Schools,verbose_name='所属学校',on_delete=models.CASCADE,db_constraint=models.CASCADE)

    def __str__(self):
        return self.department_name

    class Meta():
        verbose_name = '学院'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s


class Majors(models.Model):
    major_id = models.AutoField(verbose_name='编号',primary_key=True)
    major_name = models.CharField(verbose_name='专业名称',max_length=50)
    major_status = models.IntegerField(verbose_name='专业状态',choices=status,default=1)
    department = models.ForeignKey(Departments,verbose_name='所属学院',on_delete=models.CASCADE,db_constraint=models.CASCADE)

    def __str__(self):
        return self.major_name

    class Meta():
        verbose_name = '专业'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s


class Classes(models.Model):
    class_id = models.AutoField(verbose_name='编号', primary_key=True)
    class_name = models.CharField(verbose_name='班级名称', max_length=50)
    class_status = models.IntegerField(verbose_name='班级状态', choices=status,default=1)
    major = models.ForeignKey(Majors, verbose_name='所属专业', on_delete=models.CASCADE,db_constraint=models.CASCADE)

    def __str__(self):
        return self.class_name

    class Meta():
        verbose_name = '班级'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s


class Admins(models.Model):
    admin_id = models.AutoField(verbose_name='编号',primary_key=True)
    admin_name = models.CharField(verbose_name='用户名',max_length=30)
    admin_password = models.CharField(verbose_name='密码',max_length=20)
    admin_phone = models.CharField(verbose_name='手机号',default='13771000000',max_length=11)
    user_type = models.IntegerField(verbose_name='用户类型', choices=types,default=1)
    admin_status = models.IntegerField(verbose_name='管理员状态',choices=status,default=1)
    school = models.ForeignKey(Schools,verbose_name='所属学校',on_delete=models.CASCADE,db_constraint=models.CASCADE)

    def __str__(self):
        return self.admin_name

    class Meta():
        verbose_name = '系统管理员'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s


class Chargers(models.Model):
    charger_id = models.AutoField(verbose_name='编号', primary_key=True)
    charger_name = models.CharField(verbose_name='用户名', max_length=30)
    charger_password = models.CharField(verbose_name='密码',max_length=20)
    user_type = models.IntegerField(verbose_name='用户类型', choices=types, default=2)
    charger_phone = models.CharField(verbose_name='手机号码',default='13771000000',max_length=11)
    charger_status = models.IntegerField(verbose_name='负责人状态', choices=status,default=1)
    school = models.ForeignKey(Schools,verbose_name='所属学校',on_delete=models.CASCADE,db_constraint=models.CASCADE)

    def __str__(self):
        return self.charger_name

    class Meta():
        verbose_name = '老师'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s


class Students(models.Model):
    student_id = models.AutoField(verbose_name='编号',primary_key=True)
    student_no = models.CharField(verbose_name='学号',max_length=20)
    student_name = models.CharField(verbose_name='学生姓名',max_length=30)
    student_password = models.CharField(verbose_name='密码',max_length=20)
    student_phone = models.CharField(verbose_name='手机号',default='13771000000',max_length=11)
    classes = models.ForeignKey(Classes,verbose_name='所属班级', on_delete=models.CASCADE,db_constraint=models.CASCADE)
    user_type = models.IntegerField(verbose_name='用户类型', choices=types, default=3)
    student_status = models.IntegerField(verbose_name='学生状态',choices=status,default=1)

    def __str__(self):
        return self.student_name

    class Meta():
        verbose_name = '学生'  # 末尾加s
        verbose_name_plural = verbose_name  # 末尾不加s


class AdminToken(models.Model):
    user = models.OneToOneField(to='Admins', on_delete=models.CASCADE)
    token = models.CharField(max_length=64)


class ChargeToken(models.Model):
    user = models.OneToOneField(to='Chargers', on_delete=models.CASCADE)
    token = models.CharField(max_length=64)


class StudentToken(models.Model):
    user = models.OneToOneField(to='Students', on_delete=models.CASCADE)
    token = models.CharField(max_length=64)

