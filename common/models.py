#coding: utf-8

from random import randint

from django.db import models
from django.utils.encoding import smart_unicode
from django.db.models.signals import post_save


class BaseModel(models.Model):
    rid = models.BigIntegerField(u'编号', null=True, blank=True, unique=True)
    created_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    last_modified = models.DateTimeField(u'最近更新时间', auto_now=True)
    
    class Meta:
        abstract = True

    def __unicode__(self):
        if hasattr(self, 'name'):
            return smart_unicode(self.name)
        return u'%s'%self.id


def post_save_base_model(sender, instance, created, **kwargs):
    if created and isinstance(instance, BaseModel):
        instance.rid = int('%d%d' % (instance.id, randint(1000, 9999)))
        instance.save()

post_save.connect(post_save_base_model)
