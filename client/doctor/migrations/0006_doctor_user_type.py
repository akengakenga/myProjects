# Generated by Django 2.2.7 on 2020-02-20 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('president', '0005_president_user_type'),
        ('doctor', '0005_auto_20200220_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='user_type',
            field=models.ForeignKey(db_constraint=django.db.models.deletion.CASCADE, default=2, on_delete=django.db.models.deletion.CASCADE, to='president.UserType', verbose_name='类型'),
        ),
    ]