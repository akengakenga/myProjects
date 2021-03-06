# Generated by Django 2.2.7 on 2020-02-24 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0008_auto_20200224_1703'),
        ('doctor', '0013_auto_20200224_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treat',
            fields=[
                ('treat_id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('treat_time', models.DateTimeField(auto_now=True, verbose_name='治疗日期')),
                ('treat_problem', models.CharField(max_length=500, verbose_name='病因')),
                ('doctor', models.ForeignKey(db_constraint=django.db.models.deletion.CASCADE, on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor', verbose_name='主治医生')),
                ('patient', models.ForeignKey(db_constraint=django.db.models.deletion.CASCADE, on_delete=django.db.models.deletion.CASCADE, to='patient.Patient', verbose_name='病人')),
                ('register', models.ForeignKey(db_constraint=django.db.models.deletion.CASCADE, on_delete=django.db.models.deletion.CASCADE, to='patient.Register', verbose_name='挂号单')),
            ],
            options={
                'verbose_name': '出诊信息',
                'verbose_name_plural': '出诊信息',
            },
        ),
    ]
