# Generated by Django 2.2.7 on 2020-02-24 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('president', '0013_auto_20200224_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertype',
            old_name='user_id',
            new_name='type_id',
        ),
        migrations.AlterField(
            model_name='president',
            name='user_type',
            field=models.ForeignKey(db_constraint=django.db.models.deletion.CASCADE, default=1, on_delete=django.db.models.deletion.CASCADE, to='president.UserType', to_field='type_id', verbose_name='用户类型'),
        ),
    ]
