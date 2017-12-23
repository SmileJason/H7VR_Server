# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vr3d', '0006_vr3d_designer_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='vr3d',
            name='view_count',
            field=models.PositiveIntegerField(default=10, verbose_name='\u6d4f\u89c8\u91cf'),
        ),
    ]
