# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django.core.validators
import django.contrib.auth.models
import account.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='VRUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(upload_to=account.models.user_img_path, null=True, verbose_name='\u56fe\u7247', blank=True)),
                ('type', models.CharField(default=b'2', max_length=2, verbose_name='\u7528\u6237\u7c7b\u578b', choices=[(b'0', '\u8bbe\u8ba1\u5e08'), (b'1', '\u6ce8\u518c\u7528\u6237'), (b'2', '\u666e\u901a\u7ba1\u7406\u5458')])),
                ('address', models.CharField(max_length=256, null=True, verbose_name='\u5730\u5740', blank=True)),
                ('phone', models.CharField(max_length=64, null=True, verbose_name='\u56fa\u5b9a\u7535\u8bdd', blank=True)),
                ('mobile', models.CharField(db_index=True, max_length=64, null=True, verbose_name='\u624b\u673a\u53f7\u7801', blank=True)),
                ('security', models.CharField(default=b'1', max_length=2, verbose_name='\u5b89\u5168\u7ed1\u5b9a', choices=[(b'1', '\u672a\u7ed1\u5b9a'), (b'2', '\u90ae\u4ef6'), (b'3', '\u624b\u673a'), (b'5', '\u624b\u673a/\u90ae\u7bb1')])),
                ('gender', models.CharField(default=b'0', max_length=1, verbose_name='\u6027\u522b', choices=[(b'0', '\u672a\u6307\u5b9a'), (b'm', '\u7537'), (b'f', '\u5973')])),
                ('birthday', models.DateField(null=True, verbose_name='\u751f\u65e5', blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'account_user',
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
