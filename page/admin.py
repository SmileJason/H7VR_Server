# coding=utf-8
from django.contrib import admin

from page.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'time_display',
                    'order', 'status', 'created_time')
    list_filter = ('type', 'status')
    search_fields = ('title',)

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == 'type':
            if request.user.is_designer:
                kwargs['choices'] = [
                    ('0', u'未分类'), ('md', u'活动页面-移动版'), ('hd', u'活动页面-桌面版'), ]
        return super(PageAdmin, self).formfield_for_choice_field(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super(PageAdmin, self).get_queryset(request)
        return qs

admin.site.register(Page, PageAdmin)
