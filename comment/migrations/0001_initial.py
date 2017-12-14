# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PageComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
                ('fake_time', models.DateTimeField(help_text='\u5982\u679c\u4e3a\u7a7a\uff0c\u5219\u663e\u793a\u521b\u5efa\u65f6\u95f4', null=True, verbose_name='\u663e\u793a\u65f6\u95f4', blank=True)),
                ('fake_user', models.CharField(help_text='\u5efa\u8bae\u586b\u5199\u5e26\u661f\u53f7\u7684\u90ae\u7bb1\uff0c\u4f8b\u5982yi8***@163.com\u3002\u5982\u679c\u4e3a\u7a7a\uff0c\u5219\u663e\u793a\u7528\u6237\u7684\u540d\u79f0', max_length=63, null=True, verbose_name='\u663e\u793a\u7528\u6237\u540d', blank=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='\u6700\u8fd1\u66f4\u65b0\u65f6\u95f4')),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'page_comment',
                'verbose_name': '\u6587\u7ae0\u8bc4\u4ef7',
                'verbose_name_plural': '\u6587\u7ae0\u8bc4\u4ef7',
            },
        ),
    ]
