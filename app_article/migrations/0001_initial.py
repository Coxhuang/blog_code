# Generated by Django 2.0.7 on 2019-12-22 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=64, verbose_name='标题')),
                ('subtitle', models.CharField(default='', max_length=64, verbose_name='副标题')),
                ('content', models.TextField(default='', verbose_name='内容')),
                ('readcount', models.IntegerField(default=0, verbose_name='阅读量')),
                ('createdate', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updatedate', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('state', models.IntegerField(choices=[(0, '草稿箱'), (1, '公开'), (2, '秘密'), (3, '已删除')], default=0, verbose_name='文章状态')),
                ('image', models.TextField(default='', verbose_name='文章图片base64二进制流')),
                ('istop', models.IntegerField(choices=[(0, '正常'), (1, '置顶')], default=0, verbose_name='置顶')),
                ('tag', models.CharField(default='[]', max_length=127, verbose_name='标签')),
                ('category', models.CharField(default='{}', max_length=127, verbose_name='文章类别')),
            ],
        ),
    ]
