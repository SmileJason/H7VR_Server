#coding: utf-8

from django.db import models
from django.utils.encoding import smart_unicode

from common.utils.images import uuid_image_path, get_image

def page_img_path(instance, filename):
    return uuid_image_path(filename, 'page')

PAGE_TYPES = (
    ('0', u'案例'),
    ('1', u'客厅'),
    ('2', u'卧室'),
    ('3', u'餐厅'),
    ('4', u'儿童房'),
    ('5', u'其他'),
)

PAGE_STATUS_ACTIVE = '2'
PAGE_STATUS = (
    ('1', u'草稿'),
    (PAGE_STATUS_ACTIVE, u'生效'),
)

class Page(models.Model):
    title = models.CharField(u'标题', max_length=128)
    abstract = models.CharField(u'摘要', max_length=256, null=True, blank=True)
    thumb = models.ImageField(u'封面', upload_to=page_img_path, null=True, blank=True, help_text=u'建议大小为820x400')
    slug = models.SlugField(u'唯一路径', max_length=254, unique=True)
    type = models.CharField(u'类型', choices=PAGE_TYPES, default='0', max_length=2)
    status = models.CharField(u'状态', choices=PAGE_STATUS, default='1', max_length=1)
    order = models.PositiveIntegerField(u'排序', default=100, help_text=u'从小到大显示,相同顺序按照[显示发布时间]排序')
    time_display = models.DateTimeField(u'显示发布时间')
    content = models.TextField(u'内容')
    created_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    last_modified = models.DateTimeField(u'最近更新时间', auto_now=True)
    
    class Meta:
        db_table = 'page'
        verbose_name = u'文章发布'
        verbose_name_plural = u'文章发布'

    def __unicode__(self):
        return smart_unicode(self.title)

    @property
    def thumb_url(self):
        return get_image(self.thumb, 200, 150) if self.thumb else ''

