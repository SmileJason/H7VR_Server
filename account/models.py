#coding: utf-8
import hashlib
import random

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import smart_unicode
from django.core.exceptions import ValidationError
from common.utils.images import get_image, uuid_image_path

def user_img_path(instance, filename):
    return uuid_image_path(filename, 'user')


USER_TYPES = (
    ('0', u'设计师'),
    ('1', u'注册用户'),
    ('2', u'普通管理员'),
)

USER_SECURITIES = (
    ('1', u'未绑定'),
    ('2', u'邮件'),
    ('3', u'手机'),
    ('5', u'手机/邮箱'),
)

USER_SECURITY_NONE = '1'
USER_SECURITY_EMAIL = '2'
USER_SECURITY_MOBILE = '3'

USER_GENDERS = (
    ('0', u'未指定'),
    ('m', u'男'),
    ('f', u'女')
)

class VRUser(AbstractUser):
    avatar = models.ImageField(u'图片', upload_to=user_img_path, null=True, blank=True)
    type = models.CharField(u'用户类型', choices=USER_TYPES, default='2', max_length=2)
    address = models.CharField(u'地址', max_length=256, blank=True, null=True)
    phone = models.CharField(u'固定电话', max_length=64, blank=True, null=True)
    mobile = models.CharField(u'手机号码', max_length=64, blank=True, null=True, db_index=True)
    security = models.CharField(u'安全绑定', choices=USER_SECURITIES, default='1', max_length=2)
    gender = models.CharField(u'性别', choices=USER_GENDERS, default='0', max_length=1)
    birthday = models.DateField(u'生日', blank=True, null=True)

    class Meta:
        db_table = 'account_user'
        verbose_name = u'用户'
        verbose_name_plural = u'用户'

    def __unicode__(self):
        if self.is_customer:
            return '#%d' % self.id
        return smart_unicode(self.display_name)
    
    @property
    def avatar_path(self):
        if self.avatar:
            return get_image(self.avatar, 40, 40, water_mark=False)
        return '/static/img/avatar0.png'

    @property
    def big_avatar_path(self):
        if self.avatar:
            return get_image(self.avatar, 200, 200, water_mark=False)
        return '/static/img/avatar0.png'

    @property    
    def activate_code(self):
        random_code = str(random.randint(100000, 999999))
        email_md5 = hashlib.md5(self.email).hexdigest()
        return '%s%d-%s%s-%s%s' % (random_code[:2], self.id, random_code[2:4], email_md5[4:8], random_code[4:6], email_md5[18:26])

    def is_activate_code(self, code):
        email_md5 = hashlib.md5(self.email).hexdigest()
        try:
            uid, md1, md2 = code.split('-')
            return uid[2:]==str(self.id) and md1[2:]==email_md5[4:8] and md2[2:]==email_md5[18:26]
        except:
            return False

    @property
    def is_login(self):
        return self.is_customer and self.is_authenticated()

    @property
    def is_customer(self):
        return '1' == self.type

    @property
    def display_name(self):  # first is nick, last is real
        return self.first_name or self.username

    def secure_email(self):
        if not self.email:
            return ''
        f,s = self.email.split('@')
        n = len(f)/3
        if len(f) < 3:
            return '%s@%s' % ('*'*len(f), s)
        if len(s) < 8:
            return '{0}{1}{2}@{3}'.format(f[:n], "*"*(len(f)-2*n), f[-n:], s)
        return '{0}{1}{2}@***{3}'.format(f[:n], "*"*(len(f)-2*n), f[-n:], s[3:])

    def secure_mobile(self):
        if not self.mobile:
            return ''
        return '%s***%s' % (self.mobile[:3], self.mobile[-3:])

    def secure_name(self):
        if self.first_name:
            return self.first_name
        if self.email:
            return self.secure_email()
        if self.mobile:
            return self.secure_mobile()
        return u'匿名用户'

    @property
    def is_designer(self):
        return self.type == '0'

    @property
    def can_edit_images(self):
        return self.is_superuser or self.is_designer

    def validate_unique(self, exclude=None):
        email_exist = VRUser.objects.filter(email=self.email).exclude(id=self.id).exists()
        mobile_exist = VRUser.objects.filter(mobile=self.mobile).exclude(id=self.id).exists()
        if email_exist and self.email:
            raise ValidationError({'email': [u'该邮箱“%s”已被注册，请换一个。' % self.email],})
        elif mobile_exist and self.mobile:
            raise ValidationError({'mobile': [u'该手机号“%s”已被注册，请换一个。' % self.mobile],})
 
        return super(VRUser, self).validate_unique(exclude)
