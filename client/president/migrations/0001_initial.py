# Generated by Django 2.2.7 on 2020-02-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='President',
            fields=[
                ('pre_id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('pre_name', models.CharField(max_length=10, verbose_name='姓名')),
                ('pre_password', models.CharField(max_length=20, verbose_name='mim')),
            ],
        ),
    ]