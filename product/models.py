# coding: utf-8
from django.db import models
from django.utils.encoding import smart_unicode
from common.utils.images import get_image, uuid_image_path

def tag_img_path(instance, filename):
    return uuid_image_path(filename, 'tag')

TAG_CATEGORY_TYPES = (
    ('1', u'按产品风格'),
    ('2', u'按使用区域'),
)

class TagCategory(models.Model):
    name = models.CharField(u'名称', max_length=32)
    type = models.CharField(
        u'一级菜单', choices=TAG_CATEGORY_TYPES, default='0', max_length=2)
    order = models.PositiveSmallIntegerField(
        u'排序', default=50, help_text=u'从小到大显示，顺序相同的按最近修改时间显示')
    cover = models.ImageField(
        u'图片', upload_to=tag_img_path, null=True, blank=True)

    objects = models.Manager()

    class Meta:
        db_table = 'product_tag_category'
        verbose_name = u'产品-标签二级菜单'
        verbose_name_plural = u'产品-标签二级菜单'
        ordering = ('order',)

    def get_cover(self):
        if self.cover:
            return get_image(self.cover, 250)
        return ''

    def preview_admin(self):
        if self.cover:
            return '<a target="_blank" href="%(url)s"><img style="border:1px solid #ccc;padding:2px;max-width:150px;" src="%(url)s"/></a>' % {'url': get_image(self.cover, 150)}
        return ''
    preview_admin.short_description = u'图片预览'
    preview_admin.allow_tags = True

    def __unicode__(self):
        return '%s>%s' % (self.get_type_display(), smart_unicode(self.name))


TAG_TYPES = (
    ('0', u'-'),
    ('2', u'材质'),
    ('3', u'使用功能'),
)


class Tag(models.Model):
    category = models.ForeignKey(TagCategory, verbose_name=u'一/二级菜单',
                                 null=True, blank=True, help_text=u'归类可以作为【一级导航】，例如 餐厅')
    name = models.CharField(u'名称', max_length=32)
    type = models.CharField(u'类型', choices=TAG_TYPES,
                            default='0', max_length=2)
    cover = models.ImageField(
        u'图片', upload_to=tag_img_path, null=True, blank=True)
    parent = models.ForeignKey('self', related_name='subs',
                               verbose_name=u'上一级', null=True, blank=True, help_text=u'用户子机上的导航栏')
    order = models.PositiveSmallIntegerField(
        u'排序', default=50, help_text=u'从小到大显示，顺序相同的按最近修改时间显示')
    created_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    last_modified = models.DateTimeField(u'最近更新时间', auto_now=True)

    objects = models.Manager()

    def preview_admin(self):
        if self.cover:
            return '<a target="_blank" href="%(url)s"><img style="border:1px solid #ccc;padding:2px;max-width:150px;" src="%(url)s"/></a>' % {'url': get_image(self.cover, 150)}
        return ''
    preview_admin.short_description = u'图片预览'
    preview_admin.allow_tags = True

    class Meta:
        db_table = 'product_tag'
        verbose_name = u'产品-标签'
        verbose_name_plural = u'产品-标签'
        ordering = ('order',)

    def get_cover(self):
        if self.cover:
            return get_image(self.cover, 250)
        return ''

    def __unicode__(self):
        prefix = ''
        if self.category:
            prefix = '%s>' % smart_unicode(self.category)
        elif self.type:
            prefix = '%s/' % smart_unicode(self.get_type_display())
        return '%s%s' % (prefix, smart_unicode(self.name))
