# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import page.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name='\u6807\u9898')),
                ('abstract', models.CharField(max_length=256, null=True, verbose_name='\u6458\u8981', blank=True)),
                ('thumb', models.ImageField(help_text='\u5efa\u8bae\u5927\u5c0f\u4e3a820x400', upload_to=page.models.page_img_path, null=True, verbose_name='\u7f29\u7565\u56fe', blank=True)),
                ('slug', models.SlugField(unique=True, max_length=254, verbose_name='\u552f\u4e00\u8def\u5f84')),
                ('type', models.CharField(default=b'0', max_length=2, verbose_name='\u7c7b\u578b', choices=[(b'0', '\u6848\u4f8b'), (b'1', '\u5ba2\u5385'), (b'2', '\u5367\u5ba4'), (b'3', '\u9910\u5385'), (b'4', '\u513f\u7ae5\u623f'), (b'5', '\u5176\u4ed6')])),
                ('status', models.CharField(default=b'1', max_length=1, verbose_name='\u72b6\u6001', choices=[(b'1', '\u8349\u7a3f'), (b'2', '\u751f\u6548')])),
                ('order', models.PositiveIntegerField(default=100, help_text='\u4ece\u5c0f\u5230\u5927\u663e\u793a,\u76f8\u540c\u987a\u5e8f\u6309\u7167[\u663e\u793a\u53d1\u5e03\u65f6\u95f4]\u6392\u5e8f', verbose_name='\u6392\u5e8f')),
                ('time_display', models.DateTimeField(verbose_name='\u663e\u793a\u53d1\u5e03\u65f6\u95f4')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='\u6700\u8fd1\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'db_table': 'page_static',
                'verbose_name': '\u9875\u9762\u53d1\u5e03',
                'verbose_name_plural': '\u9875\u9762\u53d1\u5e03',
            },
        ),
    ]
