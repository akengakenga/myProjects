# Generated by Django 2.2.7 on 2020-02-23 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_auto_20200223_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='user_type',
            field=models.ForeignKey(db_constraint=django.db.models.deletion.CASCADE, default=3, on_delete=django.db.models.deletion.CASCADE, to='president.UserType', to_field='user_id', verbose_name='类型'),
        ),
    ]
