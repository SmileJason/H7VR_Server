# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vr3d', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vr3d',
            options={'verbose_name': 'VR\u4f53\u9a8c\u9986', 'verbose_name_plural': 'VR\u4f53\u9a8c\u9986'},
        ),
        migrations.AlterModelTable(
            name='vr3d',
            table='vr3d',
        ),
    ]
