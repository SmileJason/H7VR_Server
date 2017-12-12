# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u540d\u79f0')),
                ('type', models.CharField(default=b'0', max_length=2, verbose_name='\u7c7b\u578b', choices=[(b'0', '-'), (b'2', '\u6750\u8d28'), (b'3', '\u4f7f\u7528\u529f\u80fd')])),
                ('cover', models.ImageField(upload_to=product.models.tag_img_path, null=True, verbose_name='\u56fe\u7247', blank=True)),
                ('order', models.PositiveSmallIntegerField(default=50, help_text='\u4ece\u5c0f\u5230\u5927\u663e\u793a\uff0c\u987a\u5e8f\u76f8\u540c\u7684\u6309\u6700\u8fd1\u4fee\u6539\u65f6\u95f4\u663e\u793a', verbose_name='\u6392\u5e8f')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='\u6700\u8fd1\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'ordering': ('order',),
                'db_table': 'product_tag',
                'verbose_name': '\u4ea7\u54c1-\u6807\u7b7e',
                'verbose_name_plural': '\u4ea7\u54c1-\u6807\u7b7e',
            },
        ),
        migrations.CreateModel(
            name='TagCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u540d\u79f0')),
                ('type', models.CharField(default=b'0', max_length=2, verbose_name='\u4e00\u7ea7\u83dc\u5355', choices=[(b'1', '\u6309\u4ea7\u54c1\u98ce\u683c'), (b'2', '\u6309\u4f7f\u7528\u533a\u57df')])),
                ('order', models.PositiveSmallIntegerField(default=50, help_text='\u4ece\u5c0f\u5230\u5927\u663e\u793a\uff0c\u987a\u5e8f\u76f8\u540c\u7684\u6309\u6700\u8fd1\u4fee\u6539\u65f6\u95f4\u663e\u793a', verbose_name='\u6392\u5e8f')),
                ('cover', models.ImageField(upload_to=product.models.tag_img_path, null=True, verbose_name='\u56fe\u7247', blank=True)),
            ],
            options={
                'ordering': ('order',),
                'db_table': 'product_tag_category',
                'verbose_name': '\u4ea7\u54c1-\u6807\u7b7e\u4e8c\u7ea7\u83dc\u5355',
                'verbose_name_plural': '\u4ea7\u54c1-\u6807\u7b7e\u4e8c\u7ea7\u83dc\u5355',
            },
        ),
        migrations.AddField(
            model_name='tag',
            name='category',
            field=models.ForeignKey(blank=True, to='product.TagCategory', help_text='\u5f52\u7c7b\u53ef\u4ee5\u4f5c\u4e3a\u3010\u4e00\u7ea7\u5bfc\u822a\u3011\uff0c\u4f8b\u5982 \u9910\u5385', null=True, verbose_name='\u4e00/\u4e8c\u7ea7\u83dc\u5355'),
        ),
        migrations.AddField(
            model_name='tag',
            name='parent',
            field=models.ForeignKey(related_name='subs', blank=True, to='product.Tag', help_text='\u7528\u6237\u5b50\u673a\u4e0a\u7684\u5bfc\u822a\u680f', null=True, verbose_name='\u4e0a\u4e00\u7ea7'),
        ),
    ]
