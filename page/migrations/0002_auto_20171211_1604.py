# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': '\u6587\u7ae0\u53d1\u5e03', 'verbose_name_plural': '\u6587\u7ae0\u53d1\u5e03'},
        ),
        migrations.AlterModelTable(
            name='page',
            table='page',
        ),
    ]
