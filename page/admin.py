# coding=utf-8
from django.contrib import admin

from page.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'time_display',
                    'order', 'status', 'created_time')
    list_filter = ('type', 'status')
    search_fields = ('title',)

    def get_queryset(self, request):
        qs = super(PageAdmin, self).get_queryset(request)
        return qs
admin.site.register(Page, PageAdmin)
