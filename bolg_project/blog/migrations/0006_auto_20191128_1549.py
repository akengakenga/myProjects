# Generated by Django 2.2.7 on 2019-11-28 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191128_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='uinf_avatar',
            field=models.ImageField(blank=True, default='avatar/default.png', max_length=200, null=True, upload_to='static/avatar/%Y/%m', verbose_name='用户头像'),
        ),
    ]
