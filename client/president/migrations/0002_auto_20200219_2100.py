# Generated by Django 2.2.7 on 2020-02-19 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('president', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='president',
            options={'verbose_name': '院长', 'verbose_name_plural': '院长'},
        ),
        migrations.AlterField(
            model_name='president',
            name='pre_password',
            field=models.CharField(max_length=20, verbose_name='密码'),
        ),
    ]
