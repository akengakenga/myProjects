# Generated by Django 2.2.7 on 2020-03-20 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_activities_charger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activities',
            name='school',
        ),
    ]
