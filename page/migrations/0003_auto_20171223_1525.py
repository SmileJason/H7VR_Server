# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import page.models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20171211_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='thumb',
            field=models.ImageField(help_text='\u5efa\u8bae\u5927\u5c0f\u4e3a820x400', upload_to=page.models.page_img_path, null=True, verbose_name='\u5c01\u9762', blank=True),
        ),
    ]
