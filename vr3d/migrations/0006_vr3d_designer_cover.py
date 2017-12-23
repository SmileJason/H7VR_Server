# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import vr3d.models


class Migration(migrations.Migration):

    dependencies = [
        ('vr3d', '0005_vr3d_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='vr3d',
            name='designer_cover',
            field=models.ImageField(upload_to=vr3d.models.vr3d_img_path, null=True, verbose_name='\u8bbe\u8ba1\u5e08\u5c01\u9762', blank=True),
        ),
    ]
