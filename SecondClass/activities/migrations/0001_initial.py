# Generated by Django 2.2.7 on 2020-03-18 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityTypes',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('type_name', models.CharField(max_length=50, verbose_name='活动类型')),
                ('type_status', models.IntegerField(choices=[(1, '已注册'), (0, '未注册')], default=1, verbose_name='状态')),
            ],
            options={
                'verbose_name': '活动类型',
                'verbose_name_plural': '活动类型',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('notice_id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('notice_title', models.CharField(max_length=50, verbose_name='公告标题')),
                ('notice_content', models.CharField(max_length=2000, verbose_name='公告内容')),
                ('notice_create_time', models.DateTimeField(auto_now_add=True, verbose_name='公告创建时间')),
                ('notice_status', models.IntegerField(choices=[(1, '已注册'), (0, '未注册')], verbose_name='公告状态')),
                ('creater', models.ForeignKey(db_constraint=django.db.models.deletion.CASCADE, on_delete=django.db.models.deletion.CASCADE, to='logManager.Admins', verbose_name='公告创建人')),
            ],
        ),
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('activity_id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('activity_name', models.CharField(max_length=50, verbose_name='活动名称')),
                ('activity_description', models.CharField(max_length=1000, verbose_name='活动简介')),
                ('activity_img', models.ImageField(default='activity/default.png', upload_to='activity/%Y/%m', verbose_name='活动图片')),
                ('activity_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='活动地点')),
                ('activity_start_time', models.DateTimeField(verbose_name='活动开始时间')),
                ('activity_end_time', models.DateTimeField(verbose_name='活动结束时间')),
                ('activity_max_size', models.IntegerField(verbose_name='容纳人数')),
                ('activity_attend_size', models.IntegerField(default=0, verbose_name='已报名人数')),
                ('activity_credit', models.FloatField(verbose_name='活动学分')),
                ('activity_status', models.IntegerField(choices=[(0, '未激活'), (1, '未开始'), (2, '进行中'), (3, '已经结束')], default=1, verbose_name='活动状态')),
                ('activity_type', models.ForeignKey(db_constraint=django.db.models.deletion.CASCADE, on_delete=django.db.models.deletion.CASCADE, to='activities.ActivityTypes', verbose_name='活动类型')),
                ('creater', models.ForeignKey(db_constraint=django.db.models.deletion.CASCADE, on_delete=django.db.models.deletion.CASCADE, to='logManager.Admins', verbose_name='活动创建人')),
            ],
            options={
                'verbose_name': '活动',
                'verbose_name_plural': '活动',
            },
        ),
    ]