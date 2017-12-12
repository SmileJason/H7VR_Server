# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vr3d', '0003_auto_20171211_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vr3d',
            name='slug',
            field=models.SlugField(unique=True, max_length=254, verbose_name='\u552f\u4e00\u8def\u5f84'),
        ),
    ]
