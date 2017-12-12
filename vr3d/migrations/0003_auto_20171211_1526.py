# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vr3d', '0002_auto_20171211_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vr3d',
            name='slug',
            field=models.CharField(unique=True, max_length=254, verbose_name='\u552f\u4e00\u8def\u5f84'),
        ),
    ]
