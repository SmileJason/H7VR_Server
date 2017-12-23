# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vr3d', '0004_auto_20171211_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='vr3d',
            name='link',
            field=models.CharField(max_length=256, null=True, verbose_name='\u94fe\u63a5', blank=True),
        ),
    ]
