# Generated by Django 2.2.7 on 2020-03-20 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0008_auto_20200321_0501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stuedntactivity',
            old_name='activity_id',
            new_name='activity',
        ),
        migrations.RenameField(
            model_name='stuedntactivity',
            old_name='student_id',
            new_name='student',
        ),
    ]
