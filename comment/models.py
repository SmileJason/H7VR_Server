#coding: utf-8

from django.db import models

from account.models import VRUser

class PageComment(models.Model):
    user = models.ForeignKey(VRUser, verbose_name=u'用户', null=True, blank=True)
    content = models.TextField(u'评论内容')
    fake_time = models.DateTimeField(u'显示时间', null=True, blank=True, help_text=u'如果为空，则显示创建时间')
    fake_user = models.CharField(u'显示用户名', max_length=63, null=True, blank=True, help_text=u'建议填写带星号的邮箱，例如yi8***@163.com。如果为空，则显示用户的名称')
    created_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    last_modified = models.DateTimeField(u'最近更新时间', auto_now=True)

    class Meta:
        db_table = 'page_comment'
        verbose_name = u'文章评价'
        verbose_name_plural = u'文章评价'

    def __unicode__(self):
        return '%s' % self.id
