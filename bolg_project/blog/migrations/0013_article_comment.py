# Generated by Django 2.2.7 on 2019-11-29 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20191129_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('art_id', models.AutoField(primary_key=True, serialize=False, verbose_name='文章ID')),
                ('art_title', models.CharField(max_length=200, verbose_name='标题')),
                ('art_content', models.TextField(verbose_name='正文')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comm_id', models.AutoField(primary_key=True, serialize=False, verbose_name='评论ID')),
                ('comm_content', models.CharField(max_length=100, verbose_name='评论内容')),
                ('art_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
            ],
        ),
    ]