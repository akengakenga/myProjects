# Generated by Django 2.2.7 on 2019-12-02 10:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20191130_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='art_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comm_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间'),
        ),
    ]
