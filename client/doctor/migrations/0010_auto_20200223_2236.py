# Generated by Django 2.2.7 on 2020-02-23 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0009_auto_20200221_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='user_type',
            field=models.ForeignKey(db_constraint=django.db.models.deletion.CASCADE, default=2, on_delete=django.db.models.deletion.CASCADE, to='president.UserType', to_field='user_id', verbose_name='类型'),
        ),
    ]