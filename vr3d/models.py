# coding: utf-8
from django.db import models
from product.models import TagCategory
from account.models import VRUser
from django.utils.encoding import smart_unicode

from common.utils.images import uuid_image_path, get_image


def vr3d_img_path(instance, filename):
    return uuid_image_path(filename, 'vr3d')


PAGE_STATUS = (
    ('1', u'草稿'),
    ('2', u'生效'),
)


class VR3D(models.Model):
	title = models.CharField(u'标题', max_length=128)
	abstract = models.CharField(u'摘要', max_length=256, null=True, blank=True)
	thumb = models.ImageField(u'封面', upload_to=vr3d_img_path, null=True, blank=True, help_text=u'建议大小为820X400')
	slug = models.SlugField(u'唯一路径', max_length=254, unique=True)
	link = models.CharField(u'链接', max_length=256, null=True, blank=True)
	tag = models.ManyToManyField(TagCategory, db_table='vr_tag_category_map', verbose_name=u'标签')
	status = models.CharField(u'状态', choices=PAGE_STATUS, default='1', max_length=1)
	order = models.PositiveIntegerField(u'排序', default=100, help_text=u'从小到大显示,相同顺序按照[显示发布时间]排序')
	time_display = models.DateTimeField(u'显示发布时间')
	created_time = models.DateTimeField(u'创建时间', auto_now_add=True)
	last_modified = models.DateTimeField(u'最近更新时间', auto_now=True)
	alias = models.CharField(u'设计师', max_length=128)
	creator = models.ForeignKey(VRUser, verbose_name=u'创建人', null=True, blank=True)

	class Meta:
		db_table = 'vr3d'
		verbose_name = u'VR体验馆'
		verbose_name_plural = u'VR体验馆'

	def __unicode__(self):
		return smart_unicode(self.title)

	@property
	def thumb_url(self):
		return get_image(self.thumb, 200, 150) if self.thumb else ''
